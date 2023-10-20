
import csv
import hash 
import trie
import consultas
import time
TAMTABLEJOGADORES = 3500
TAMTABLERATINGS = 10900




def constroi_jogadores():
    with open('players.csv', 'r') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        for linha in leitor_csv:
            jogador = hash.Jogador(linha['sofifa_id'], linha['name'].lower(), linha['player_positions'])
            hashJogadores.constroiTableJogadores(jogador)
            trie_nomes.insert(jogador.name,jogador.fifaId)
            posicoes = jogador.pos.lower().replace(" ","").split(",")
            for pos in posicoes:
                trie_posicoes.insert(pos,jogador.fifaId)
        

def constroi_ratings():
    with open('rating.csv', 'r') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        for linha in leitor_csv:
           hashRatings.constroiTableRatings(hashJogadores,linha['user_id'],linha['rating'],linha['sofifa_id'])


def constroi_tags():
    with open('tags.csv', 'r') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        for linha in leitor_csv:
            tag = hash.Tag(linha['user_id'], linha['sofifa_id'].lower(), linha['tag'])
            hashTags.constroiTableTags(tag)





inicio = time.time()
hashJogadores = hash.HashTable(TAMTABLEJOGADORES)
hashRatings = hash.HashTable(TAMTABLERATINGS)
hashTags = hash.HashTable(TAMTABLEJOGADORES)
trie_nomes = trie.Trie()
trie_posicoes = trie.Trie()
constroi_jogadores()
constroi_ratings()
constroi_tags()

#consultas.consulta_posicoes(trie_posicoes,hashJogadores,TAMTABLEJOGADORES)

fim = time.time()
tempo_decorrido = fim - inicio


print(f"A construção levou {tempo_decorrido:.6f} segundos para executar.")
consultas.consulta_posicoes(trie_posicoes, hashJogadores)
