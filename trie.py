class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = [None] * 31  # Uma lista de 26 elementos para as letras do alfabeto + espaço + - + ' + . + "
        self.haveChild = False
        self.is_end_of_word = False
        self.id = None

    def busca_filho(self,prefix,lista):
        node = self

        if node.is_end_of_word and node.haveChild:
            node.busca_filho_lista(prefix,lista)
            return lista.append(node.id)
        
        elif node.is_end_of_word:
            return lista.append(node.id)
        
        else:
            return node.busca_filho_lista(prefix,lista)

    def busca_filho_lista(self,prefixo,lista):
        filhos = self.children

        for node in filhos:
            if node != None:
                node.busca_filho(prefixo + node.char,lista)
        return lista
    

class Trie:
    def __init__(self):
        self.root = TrieNode(None)

    def _char_to_index(self, char):
        if char == " ":
            return 26
        elif char == "-":
            return 27
        elif char == "'":
            return 28
        elif char == ".":
            return 29
        elif char == '"':
            return 30
        return ord(char) - ord('a')

    def insert(self, nome_jogador, jogador_id):
        node = self.root
        for char in nome_jogador:
            index = self._char_to_index(char)
            if  node.children[index] == None:
                node.children[index] = TrieNode(char)
                node.haveChild = True
            node = node.children[index]
        node.is_end_of_word = True

        if node.id == None:
            node.id = jogador_id 
        elif isinstance(node.id, str):
            lista = [node.id, jogador_id]
            node.id= lista
        else:
            node.id.append(jogador_id)

    def busca_prefixo(self, word):
        node = self.root
        for char in word:
            index = self._char_to_index(char)
            if  node.children[index] == None:
                return False
            node = node.children[index]
        if node.is_end_of_word:
            return node.id 
        else:
            return node.busca_filho(word,[])