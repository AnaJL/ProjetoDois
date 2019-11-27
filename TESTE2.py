class Dado:
    def __init__(self, nomeFilme, ano, id):
        self._id = id
        self._nomeFilme = nomeFilme
        self._ano = ano

    def get_nomeFilme(self):   #Retorna nome do filme
        return self._nomeFilme

    def set_nomeFilme(self, novoNome): #Altera nome do filme
        self._nomeFilme = novoNome

    def get_ano(self):       #Retorna Ano
        return self._ano

    def set_ano(self, novoAno): #Altera Ano
        self._ano = novoAno

    def get_id(self):  #Retorna Id
        return self._id

    def set_id(self, novoId):  #Alter Id
        self._id = novoId

    def __str__(self):
        f'nome: {self.get_nomeFilme()}Id: {self.get_id} ano: {self.get_ano()}'
class No:
    def __init__(self, dado,esquerda = None, direita = None):
        self._dado = dado
        self._esquerda = esquerda
        self._direita = direita

    def get_dado(self):   #Retorna Dado
        return self._dado

    def set_dado(self, novaDado): #Altera Dado
        self._dado = novaDado

    def get_esquerda(self): #Retorna Esquerda
        return self._esquerda

    def set_esquerda(self, novoEsquerda): #Altera Esquerda
        self._esquerda = novoEsquerda

    def get_direita(self): #Retorna Direita
        return self._direita

    def set_direita(self, novoDireita): #Altera direita
        self._direita = novoDireita


class ArvoreAVL:
    def __init__(self, raiz=None, esquerda = None, direita = None):
        self._raiz = raiz
        self._esquerda = esquerda
        self._direita = direita

    def get_raiz(self):  #Retorna Raiz
        return self._raiz

    def set_raiz(self, novo): #Altera Raiz
        self._raiz = novo

    def balanco(self):   #Vê o fator de balanceamento
        altura_esquerda = 0
        altura_direita = 0
        if self._esquerda:
            altura_esquerda = self._esquerda.profundidade()
        if self._direita:
           altura_direita = self._direita.profundidade()
        return altura_esquerda - altura_direita

    def inserir(self, no):   #Insere no
        if self._raiz == None:
            self._raiz = no
        else:
            p = self._raiz
            q = p
            while q != None:
                if no.get_dado().get_nomeFilme() > p.get_dado().get_nomeFilme():
                    p = q
                    q = q.get_direita()
                    p.set_direita(no)
                else:
                    p = q
                    q = q.get_esquerda()
                    p.set_esquerda(no)
        self.executaBalanco()

    def rotacaoEsquerda(self): #Rotação para Esquerda (Negativo)
        p = self._raiz
        aux = p.get_direita()
        p.set_direita(aux.get_esquerda())
        aux.set_esquerda(p)

    def rotacaoDireita(self):  #Rotação para Direita (Positivo)
        p = self._raiz
        aux = p.get_esquerda()
        p.set_esquerda(aux.get_direita())
        aux.set_direita(p)

    def rotacaoEsquerdaDireita(self):
        self._esquerda.rotacaoEsquerda()
        self.rotacaoDireita()

    def rotacaoDireitaEsquerda(self):
        self._direita.rotacaoDireita()
        self.rotacaoEsquerda()

    def executaBalanco(self): #Executa o Balanceamento
        balanci = self.balanco()
        if balanci > 1:
            if self._esquerda.balanco() > 0:
                self.rotacaoDireita()
            else:
                self.rotacaoEsquerdaDireita()
        elif balanci < -1:
            if self._direita.balanco() < 0:
                self.rotacaoEsquerda()
            else:
                self.rotacaoDireitaEsquerda()

    def buscar_Id(self, id, atual): #Busca o Id
        pass

    def buscar_Ano(self, ano, chaves): #Busca o Ano
        pass

    def Altura(self, no): #Devolve a altura
        p = no
        if p == None:
            return -1
        if  p.get_esquerda() == None and p.get_direita() == None:
            return 0
        else:
            if self.Altura(p.get_esquerda()) > self.Altura(p.get_direita()):
                return 1 + self.Altura(p.get_esquerda())
            else:
                return 1 + self.Altura(p.get_direita())

    def OrdemAlfa(self, lista): #Deixa em ordem alfabetica
        if lista == []:
            print('Árvore Vazia')
        else:
            for i in range(len(lista)):
                for j in range(len(lista)):
                    if lista[i] < lista[j]:
                        lista[i], lista[j] = lista[j], lista[i]
            print('''ORDEM ALFABÉTICA: ''')
            for z in range(len(lista)):
                print(lista[z])
    def menu(self): #Menu
        return input(""" 
\033[31mI\033[m\033[32mFPB\033[m - \033[1;94mInstituto Federal da Paraiba \033[m
\033[1;36m=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\033[m
\033[1;34m _____________________________________________\033[m
\033[1;34m|\033[m         \033[1;36m▒█▀▄▀█ ▒█▀▀▀ ▒█▄░▒█ ▒█░▒█\033[m           \033[1;34m|\033[m
\033[1;34m|\033[m         \033[1;36m▒█▒█▒█ ▒█▀▀▀ ▒█▒█▒█ ▒█░▒█\033[m           \033[1;34m|\033[m
\033[1;34m|\033[m         \033[1;36m▒█░░▒█ ▒█▄▄▄ ▒█░░▀█ ░▀▄▄▀\033[m           \033[1;34m|  \033[m                              
\033[1;34m|_____________________________________________|\033[m                                            
\033[1;34m|\033[m \033[1;31m0) sair do Menu\033[m                             \033[1;34m|\033[m
\033[1;34m|\033[m 1) Inserir filme                            \033[1;34m|\033[m
\033[1;34m|\033[m 2) Buscar filme pelo id                     \033[1;34m|\033[m
\033[1;34m|\033[m 3) Buscar filmes pelo ano   - TODO          \033[1;34m|\033[m
\033[1;34m|\033[m 4) Listar filmes em ordem alfabética        \033[1;34m|\033[m
\033[1;34m|\033[m 5) Altura da árvore                         \033[1;34m|\033[m
\033[1;34m|\033[m 6) Exibir a árvore  - TODO                  \033[1;34m|\033[m
\033[1;34m|_____________________________________________|\033[m
\033[1;31m▸\033[m Digite sua opção: 
""")
filme = ArvoreAVL()
chaves = []
listafilmes = []
resp = filme.menu()
while resp != '0':
    if resp == '1':
        nome = input('Filme: ')
        ano = int(input('Ano: '))
        id = int(input('Chave:  '))
        if id in chaves:
            id = int(input(f'C1have {id} já existe, digite outro! '))
        filme.inserir(No(Dado(nome, ano, id)))
        chaves.append(id)
        listafilmes.append(filme)
    elif resp == '2':
        i = int(input('Chave: '))
        pass
    elif resp == '3':
        ano = int(input('Ano: '))
        pass
    elif resp == '4':
        print(filme.OrdemAlfa(listafilmes))
    elif resp == '5':
        print(filme.Altura(filme.get_raiz()))
    elif resp=='6':
        pass
    if resp not in ['0', '1', '2', '3', '4', '5', '6']:
        print('✘ Comando invalido ✘')
    resp = filme.menu()
print('fim')
