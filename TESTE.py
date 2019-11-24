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
            prof_esq = self._esquerda.profundidade()
        prof_dir = 0
        if self._direita:
            prof_dir = self._direita.profundidade()
        return prof_esq - prof_dir

    def profundidade(self):
        prof_esq = 0
        if self._esquerda:
            prof_esq = self._esquerda.profundidade()
        prof_dir = 0
        if self._direita:
            prof_dir = self._direita.profundidade()
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
        self._dado, self._id, self._direita._dado, self._direita._id = self._direita._dado, self._direita._id, self._dado, self._id
        old_esquerda = self._esquerda
        self.setaFilhos(self._direita, self._direita._direita)
        self._esquerda.setaFilhos(old_esquerda, self._esquerda._esquerda)

    def rotacaoDireita(self):
        self._dado, self._id, self._esquerda._dado, self._esquerda._id= self._esquerda._dado, self._esquerda._id, self._dado, self._id
        old_direita = self._direita
        self.setaFilhos(self._esquerda._esquerda, self._esquerda)
        self._direita.setaFilhos(self._direita._direita, old_direita)

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

    def inserir(self, elem, pos):
        if self._dado == None:
            self._dado = elem._dado
            self._id = elem._id
        elif pos == 'inte':
            if elem._id < self._id:
                if not self._esquerda:
                    self.set_esquerda(elem)
                else:
                    self._esquerda.inserir(elem, 'inte')
            else:
                if not self._direita:
                    self.set_direita(elem)
                else:
                    self._direita.inserir(elem, 'inte')
        elif pos == 'ext':
            if self._dado._id:
                if elem._id < self._dado._id:
                    if not self._esquerda:
                        self.set_esquerda(elem)
                    else:
                        self._esquerda.inserir(elem, 'inte')
                else:
                    if not self._direita:
                        self.set_direita(elem)
                    else:
                        self._direita.inserir(elem, 'inte')
            else:
                self.inserir(elem, 'inte')

        self.executaBalanco()

    def imprimeArvoreAvl(self, pos, espaco=20):
        if self._dado == None:
            print('Árvore Vazia !')
        elif pos == 'ext':
            if self._dado._id == None:
                self.imprimeArvoreAvl('int')
            else:
                print(" " * espaco + str(self._dado._id))
                if self._esquerda:
                    self._esquerda.imprimeArvoreAvl('inter', espaco - 4)
                elif self._direita:
                    self._direita.imprimeArvoreAvl('inter', espaco + 4)
        else:
            if self._id == None:
                    self.imprimeArvoreAvl('ext')
            else:
                print(" " * espaco + str(self._id))
                if self._esquerda:
                    self._esquerda.imprimeArvoreAvl('inter', espaco - 4)
                if self._direita:
                    self._direita.imprimeArvoreAvl('inter', espaco + 4)

    def buscaid(self, chave, chaves, lista):
        Inf = 0
        Sup = len(chaves) - 1
        met = 0
        while (Inf <= Sup):
            met = (Inf + Sup) // 2
            if (chaves[met] == chave):
                return lista[met].get_filmeeano()
            if (chave < chaves[met]):
                Sup = met - 1
            else:
                Inf = met + 1
        return 'Chave não encontrada'
    def buscaano(self, ano, anos, lista):
        Inf = 0
        Sup = len(anos) - 1
        met = 0
        while (Inf <= Sup):
            met = (Inf + Sup) // 2
            if (anos[met] == ano):
                for i in range(anos.count(ano)-1):
                    print(lista[met + i].get_filme())
            if (ano < anos[met]):
                Sup = met - 1
            else:
                Inf = met + 1
        if ano not in anos:
            print('Chave não encontrada')

    def menu(self):
        return input(""" 
 _____________________________________________
|         ▒█▀▄▀█ ▒█▀▀▀ ▒█▄░▒█ ▒█░▒█           |
|         ▒█▒█▒█ ▒█▀▀▀ ▒█▒█▒█ ▒█░▒█           |
|         ▒█░░▒█ ▒█▄▄▄ ▒█░░▀█ ░▀▄▄▀           |                                
| ____________________________________________|                                            
| 0) sair do Menu                             |
| 1) Inserir filme                            |
| 2) Buscar filme pelo id                     |
| 3) Buscar filmes pelo ano   - TODO          |
| 4) Listar filmes em ordem alfabética        |
| 5) Altura da árvore                         |
| 6) Exibir a árvore  - TODO                  |
|_____________________________________________|
 ▸ Digite sua opção: 
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
            arv.inserir(novo, 'ext')
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
        arv.listaalt()
    if resp not in ['0', '1', '2', '3', '4', '5', '6']:
        print('✘ Comando invalido ✘')
    resp = arv.menu()
print('Fim')