from Dados import Dado
class No:
    def __init__(self,dado = None, ide = None, filho = None, esquerda = None, direita = None):
        self._dado = dado
        self._id = ide
        self._filho = filho
        self._esquerda = esquerda
        self._direita = direita
    def get_esquerda(self):
        return self._esquerda
    def set_esquerda(self,novo):
        self._esquerda = novo
    def get_direita(self):
        return self._direita
    def set_direita(self,novo):
        self._direita = novo
    def profundidade(self):
        prof_esq = 0
        prof_dir = 0
        if self.get_esquerda():
            prof_esq = self.get_esquerda().profundidade()
        if self.get_direita():
            prof_dir = self.get_direita().profundidade()
        return max(prof_esq, prof_dir)
    def verBalanco(self):
        profundidade_esquerda = 0
        profundidade_direita = 0
        if self.get_esquerda():
           profundidade_esquerda = self.get_esquerda().profundidade()
        if self.get_direita():
            profundidade_direita = self.get_direita().profundidade()
        return profundidade_esquerda - profundidade_direita
    def Rotacionar_Esquerda(self):
        aux = self._dado.get_direita()
        self._dado.set_direita(aux._esquerda())
        aux.set_esquerda(self._dado)
        return aux
    def Rotacionar_Direita(self):
        aux = self._dado.get_esquerda()
        self._dado.set_esquerda(aux.set_direita())
        aux.set_direita(self._dado)
        return aux
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
            self._dado = elem
            return 'Foi adicionado a raiz com sucesso ! ✔'
        if pos == 'inte':
            if elem._id < self._id:
                if not self._esquerda:
                    self.set_esquerda(elem)
                else:
                    self._esquerda.inserir(elem, 'inte')
                return 'Foi adicionado com sucesso ✔!'
            else:
                if not self._direita:
                    self.set_direita(elem)
                else:
                    self._direita.inserir(elem, 'inte')
                return 'Foi adicionado com sucesso ✔!'
        if pos == 'ext':
            if elem._id < self._dado._id:
                if not self._esquerda:
                    self.set_esquerda(elem)
                else:
                    self._esquerda.inserir(elem, 'inte' )
                return 'Foi adicionado com sucesso ✔!'
            else:
                if not self._direita:
                    self.set_direita(elem)
                else:
                    self._direita.inserir(elem, 'inte')
                return 'Foi adicionado com sucesso ✔ !'

        self.Balanceamento()
    def Rotacionar_Esquerda_Direita(self):
        self.get_esquerda().Rotacionar_Esquerda()
        self.Rotacionar_Direita()
    def Rotacionar_Direita_Esquerda(self):
        self.get_direita().Rotacionar_Direita()
        self.Rotacionar_Direita()
    def Balanceamento(self):
        balancear = self.verBalanco()
        if balancear > 1:
            if self.get_esquerda().balanco() > 0:
                self.Rotacionar_Direita()
            else:
                self.Rotacionar_Esquerda_Direita()
        elif balancear < -1:
            if self.get_direita().balanco < 0:
                self.Rotacionar_Esquerda()
            else:
                self.Rotacionar_Direita_Esquerda()
    def imprimeArvoreAvl(self, pos, espaco = 10 ):
        if self._dado == None:
            print('Árvore Vazia !')
        elif pos == 'ext':
            print(" " * espaco + str(self._dado._id))
            if self._esquerda:
                self._esquerda.imprimeArvoreAvl('inter', espaco - 4)
            if self._direita:
                self._direita.imprimeArvoreAvl('inter', espaco + 4)
        else:
            print(" " * espaco + str(self._id))
            if self._esquerda:
                self._esquerda.imprimeArvoreAvl('inter', espaco - 4)
            if self._direita:
                self._direita.imprimeArvoreAvl('inter', espaco + 4)

    def buscaid(self, ide):
        if self._dado == None:
            print('Arvore Vazia')
        else:
            atual = self._dado
            while atual.dado.get_id() != ide:
                if ide < atual.dado.get_id():
                    atual = atual.left
                elif ide > atual.dado.get_id():
                    atual = atual.right
                if atual == None:
                    print('Não encontrada')
                    break
            if atual != None:
                print(atual.dado.get_filmeeano())

    def buscaano(self, ano):
        if self._dado == None:
            print('Arvore Vazia')
        else:
            atual = self._dado
            while atual.dado.get_ano() != ano:
                if ano < atual.dado.get_ano():
                    atual = atual.left
                elif ano > atual.dado.get_ano():
                    atual = atual.right
                if atual == None:
                    print('Não encontrada')
                    break
            if atual != None:
                print(atual.dado.get_filmeeano())
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
| 3) Buscar filmes pelo ano                   |
| 4) Listar filmes em ordem alfabética        |
| 5) Altura da árvore                         |
| 6) Exibir a árvore                          |
|_____________________________________________|
 
 ▸ Digite sua opção: 
""")

arv = No()
resp = arv.menu()
listachaves = []
listafilmes = []
while resp != '0':
    if resp == '1':
        filme = input('Filme: ')
        ano = int(input('Ano: '))
        chave = int(input('Chave: '))
        novo = No(Dado(filme, ano), chave)
        if chave in listachaves:
            print(f'o ID {chave} já existe !')
        else:
            listafilmes.append(filme)
            listachaves.append(chave)
            print(arv.inserir(novo, 'ext'))
    if resp == '2':
        arv.imprimeArvoreAvl('ext')
    if resp == '3':
        arv.imprimeArvoreAvl('ext')
    if resp == '4':
        arv.OrdemAlfa(listafilmes)
    if resp == '5':
        print(arv.profundidade())
    if resp == '6':
        arv.imprimeArvoreAvl('ext')
    if resp not in ['0', '1', '2', '3', '4', '5', '6']:
        print('✘ Comando invalido ✘' )
    resp = arv.menu()
print('Fim')
