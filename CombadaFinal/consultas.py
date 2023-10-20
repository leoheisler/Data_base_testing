import hash
import statistics
import trie
import copy

def consulta_nomes(trie_jog,hashJogadores):
    print("Escreva o nome do Jogador:")
    prefixo = input().lower().replace("\n","")
    jogadores_id = trie_jog.busca_prefixo(prefixo)
    with open("consulta_nomes.txt","w") as arquivo:
        if isinstance(jogadores_id,list):
            for id in jogadores_id:
                if isinstance(id,list):
                    for i in id:
                        print_jogador(hashJogadores.consultaJogador(i),arquivo)
                else:
                    print_jogador(hashJogadores.consultaJogador(id),arquivo)
        else:
            print_jogador(hashJogadores.consultaJogador(jogadores_id),arquivo)
    return

def consulta_posicoes(trie_pos,hashJogadores):
    listaJogadores = []
    print("digite o N:")
    n = int(input())
    count = 0
    print("digite a posição:")
    prefixo = input().lower().replace("\n","")
    jogadores_id = trie_pos.busca_prefixo(prefixo)

    for id in jogadores_id:
        jogador = hashJogadores.consultaJogador(id)
        jogadorCopia = copy.deepcopy(jogador)
        jogadorCopia.reviews = [float(valor) for valor in jogadorCopia.reviews]
        if len(jogador.reviews) != 0:
            jogadorCopia.reviews = statistics.mean(jogadorCopia.reviews)
            jogadorCopia.count = len(jogador.reviews)
        else:
            jogadorCopia.reviews = 0

        listaJogadores.append(jogadorCopia)

    listaJogadores_sorted = sorted(listaJogadores, key=lambda x: x.reviews, reverse=True)
    with open("consulta_posicoes.txt","w") as arquivo:
        for jogador in listaJogadores_sorted:
            if count >= n:
                break
            if jogador.count > 999:
                string = jogador.fifaId + " " + jogador.name.title() + " " + jogador.pos + " " + str(jogador.reviews) + " " + str(jogador.count) +'\n'
                arquivo.write(string)
                count = count + 1



def consulta_ratings(hashRatings,hashJogadores,userId):

    revisados_list = hashRatings.consultaRating(userId) # lista de revisoes com o fifaId e o rating preenchidos

    for revisado in revisados_list:                            #Vai na hash de jogadores e complesta as revisoes com o nome, a quantidade de reviews e a média
        jogador = hashJogadores.consultaJogador(revisado.fifaId)
        revisado.name = jogador.name
        revisado.count = len(jogador.reviews)
        for i in jogador.reviews:
            revisado.global_rating += float(i)
        revisado.global_rating = revisado.global_rating/len(jogador.reviews)
        
    revisados_sorted = sorted(revisados_list, key=lambda x: x.rating, reverse=True)
    
    count = 0
    with open("consulta_revisoes") as arquivo:
        for revisado in revisados_sorted:
            if count < 20:
                string = revisado.fifaId + " " + revisado.name + " " + str(revisado.global_rating) + " " + str(revisado.count) + " " + str(revisado.rating) + '\n'
                arquivo.write(string)
                count += 1
            else: break

def consulta_tags(hashTags, hashJogadores, listaKeyTags):
    listaKeyTags = listaKeyTags.split(' ')
    ListaDeListasIds = []
    listaIdsVericados = []
    listaJogadores = []
    for key in listaKeyTags:
        ListaDeListasIds.append(hashTags.consultaTag(key))#lista de listas com tags, uma lista para cada keytag

    for Id in ListaDeListasIds[0]: # verifica se o ID está em todas as listas
        flag = True
        for i in range(1, len(listaKeyTags)):
            if Id not in ListaDeListasIds[i]: #se o Id não estiver em algumas das outras listas, troca a flag para false
                flag = False
        if flag and Id not in listaIdsVericados:
            listaIdsVericados.append(Id)
    
    for Id in listaIdsVericados:
        listaJogadores.append(hashJogadores.consultaJogador(Id))
    
    with open("consulta_tags.txt","w") as arquivo:
        for jogador in listaJogadores:
            media = 0
            for r in jogador.reviews:
                media += float(r)/len(jogador.reviews)
            string = jogador.fifaId + " " + jogador.name.title() + " " + jogador.pos + " " +  str(media) + " " +  str(len(jogador.reviews)) + '\n'
            arquivo.write(string)
    
def print_jogador(jogador,arquivo):
    media = 0
    for num in jogador.reviews:
        media +=  float(num)
    if(len(jogador.reviews) != 0):
        media = media/len(jogador.reviews)
    string = jogador.fifaId +" " +  jogador.name.title() + " "+ jogador.pos +  " "+ str(media) + " " + str((len(jogador.reviews)) )+ '\n'
    arquivo.write(string)

