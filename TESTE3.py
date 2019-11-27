from Dados import Dado
class No:
    def __init__(self, dado=None, ide=None, ):
        self._dado = dado
        self._id = ide
        self.setaFilhos(None, None)

    def setaFilhos(self, esquerda, direita):
        self._esquerda = esquerda
        self._direita = direita

    def set_esquerda(self, novo):
        self._esquerda = novo

    def set_direita(self, novo):
        self._direita = novo

    def balanco(self):
        prof_esq = 0
        if self._esquerda:
            prof_esq = self._esquerda.alturaBalanco()
        prof_dir = 0
        if self._direita:
            prof_dir = self._direita.alturaBalanco()
        return prof_esq - prof_dir

    def alturaBalanco(self):
        prof_esq = 0
        if self._esquerda:
            prof_esq = self._esquerda.alturaBalanco()
        prof_dir = 0
        if self._direita:
            prof_dir = self._direita.alturaBalanco()
        return 1 + max(prof_esq, prof_dir)

    def altura(self):
        if self._dado == None:
            return -1
        elif self._esquerda == None and self._direita == None:
            return 0
        else:
            alt_esq = 0
            if self._esquerda:
                alt_esq = self._esquerda.altura()
            alt_dir = 0
            if self._direita:
                alt_dir = self._direita.altura()
            return 1 + max(alt_esq, alt_dir)

    def rotacaoEsquerda(self):
        sd = self._direita
        self._dado, self._id, sd._dado, sd._id = sd._dado, sd._id, self._dado, self._id
        esqant = self._esquerda
        self.setaFilhos(sd, sd._direita)
        self._esquerda.setaFilhos(esqant, self._esquerda._esquerda)

    def rotacaoDireita(self):
        se = self._esquerda
        self._dado, self._id, se._dado, se._id= se._dado, se._id, self._dado, self._id
        dirant = self._direita
        self.setaFilhos(se._esquerda, se)
        self._direita.setaFilhos(self._direita._direita, dirant)

    def rotacaoEsquerdaDireita(self):
        self._esquerda.rotacaoEsquerda()
        self.rotacaoDireita()

    def rotacaoDireitaEsquerda(self):
        self._direita.rotacaoDireita()
        self.rotacaoEsquerda()

    def executaBalanco(self):
        bal = self.balanco()
        if bal > 1:
            if self._esquerda.balanco() > 0:
                self.rotacaoDireita()
            else:
                self.rotacaoEsquerdaDireita()
        elif bal < -1:
            if self._direita.balanco() < 0:
                self.rotacaoEsquerda()
            else:
                self.rotacaoDireitaEsquerda()

    def OrdemAlfa(self, lista):
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

    def inserir(self, elem):
        if self._dado == None:
            self._dado = elem._dado
            self._id = elem._id
        elif elem._id < self._id:
            if not self._esquerda:
                self.set_esquerda(elem)
            else:
                self._esquerda.inserir(elem)
        else:
            if not self._direita:
                self.set_direita(elem)
            else:
                self._direita.inserir(elem)
        self.executaBalanco()

    def print(self, espaco=0):
        espaco = self.alturaBalanco() * 6
        espacomeio = 5
        if self.altura() == -1:
            print('Árvore Vazia')
        else:
            print(' ' * (espaco) + str(self._id))
            root = self
            if self._direita and not self._esquerda:
                espaco = espaco -3
                print(' ' * espaco + str('n') + ' ' * espacomeio + str(self._direita._id))
            if root._esquerda:
                if self._direita == None and self._esquerda == None:
                    return
                else:
                    while self._esquerda != None and self._direita != None:
                        espaco = espaco - 3
                        print(' ' * espaco + str(self._esquerda._id) + ' ' * espacomeio + str(self._direita._id))
                        self = self._esquerda
                        if  self == None:
                            break
                    while self._esquerda:
                        espaco = espaco - 3
                        print(' ' * espaco + str(self._esquerda._id) + ' ' * espacomeio + str('n'))
                        self = self._esquerda
                        if  self == None:
                            break
                    while self._direita:
                        espaco = espaco - 3
                        print(' ' * espaco + str('n') + ' ' * espacomeio + str(self._direita._id))
                        self = self._direita
                        if self == None :
                            break
            if root._direita:
                self = root._direita
                if self == None and self._esquerda == None:
                    return
                else:
                    while self._esquerda != None and self._direita != None:
                        espaco = espaco + 6
                        print(' ' * espaco + str(self._esquerda._id) + ' ' * espacomeio + str(self._direita._id))
                        self = self._esquerda
                        if  self == None:
                            break
                    while self._esquerda:
                        espaco = espaco + 6
                        print(' ' * espaco + str(self._esquerda._id) + ' ' * espacomeio + str('n'))
                        self = self._esquerda
                        if self == None:
                            break
                    while self._direita:
                        espaco = espaco + 6
                        print(' ' * espaco + str('n') + ' ' * espacomeio + str(self._direita._id))
                        self = self._direita
                        if self == None:
                            break

    def buscaid(self, chave, chaves, lista):
        for i in range(len(chaves)):
            if (chaves[i] == chave):
                return lista[i].get_filmeeano()
        return 'Chave não encontrada'

    def buscaano(self, ano, anos, lista):
        for i in range(len(anos)):
            if (anos[i] == ano):
                print(lista[i].get_filme())
        if ano not in anos:
            print('Chave não encontrada')

    def menu(self):
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
arv = No()
resp = arv.menu()
listachaves = []
listaanos = []
listafilmes = []
listaD = []
while resp != '0':
    if resp == '1':
        filme = input('Filme: ')
        ano = int(input('Ano: '))
        chave = int(input('Chave: '))
        novo = No(Dado(filme, ano), chave)
        if chave in listachaves:
            print(f'o ID {chave} já existe !')
        else:
            listaD.append(Dado(filme, ano))
            listafilmes.append(filme)
            listachaves.append(chave)
            listaanos.append(ano)
            arv.inserir(novo)
            print('Adicionado com Sucesso !')

    if resp == '2':
        ide = int(input('ID procurado : '))
        print(arv.buscaid(ide, listachaves, listaD))
    if resp == '3':
        ano = int(input('ANO procurado : '))
        arv.buscaano(ano, listaanos, listaD)
    if resp == '4':
        arv.OrdemAlfa(listafilmes)
    if resp == '5':
        print(arv.altura())
    if resp == '6':
        arv.print()
    if resp not in ['0', '1', '2', '3', '4', '5', '6']:
        print('✘ Comando invalido ✘')
    resp = arv.menu()
print('Fim')