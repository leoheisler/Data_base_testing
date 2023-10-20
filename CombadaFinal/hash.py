class Revisado:
    def __init__(self, fifaId, name, global_rating, count, rating):   
        self.fifaId = fifaId
        self.name = name
        self.global_rating = global_rating
        self.count = count
        self.rating = rating

class Jogador:
    def __init__(self,fifaId,name,pos):
        self.fifaId = fifaId
        self.name = name
        self.pos = pos
        self.reviews =[]
        self.count = 0


class Tag:
    def __init__(self,userId,fifaId,tag):
        self.userId = userId
        self.fifaId = fifaId
        self.tag = tag


class HashTable:
    def __init__(self,tam):
        self.table = [[]]*tam
        self.len = tam
        self.save = Jogador("0","A","ABABA")


    def constroiTableJogadores(self,jogador):
        index = Hash(jogador.fifaId,self.len)
        self.table[index].append(jogador)
    

    def constroiTableRatings(self,tabelaJogadores,user_id,rating,sofifa_id,):
        indexRating = Hash(user_id,self.len)
        self.table[indexRating].append([user_id,sofifa_id,rating])
        if sofifa_id != self.save.fifaId:
           self.save = tabelaJogadores.consultaJogador(sofifa_id)     
        self.save.reviews.append(rating)


    def constroiTableTags(self,tag):
        n = 0
        for char in tag.tag:
            n += ord(char)
        index = Hash(n,self.len)
        self.table[index].append(tag)


    def consultaJogador(self,Id):
        index = Hash(Id,self.len)
        for jogador in self.table[index]:
            if Id == jogador.fifaId:
                return jogador
            
    
    def consultaRating(self,Id): #Dado o Id de um usuário, devolve uma lista com os revisados
        index = Hash(Id,self.len)
        revisoes = []
        for i in self.table[index]:
            if Id == i[0]:
                revisoes.append(Revisado(i[1], "", 0, 0, float(i[2]))) #i[0] = user_id, i[1] = sofifa_id, i[2] = rating
        return revisoes
    
    def consultaTag(self,tagProcurada):
        n=0
        for char in tagProcurada:
            n+=ord(char)
        index = Hash(n,self.len)
        listaIds = []
        for tag in self.table[index]:
            if tagProcurada == tag.tag:
                listaIds.append(tag.fifaId)
        return listaIds
        
        
def Hash(Id, tamTable):
    valor = int(Id) % tamTable
    return valor

