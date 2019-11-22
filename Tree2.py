from Dados import Dado
class No:
    def __init__(self, dado):
        self.dado = dado
        self.left = None
        self.right = None

class avl:
    def __init__(self, dado=None):
        self.root = dado

    def setaFilhos(self, left, right):
        self.left= left
        self.right = right

    def profundidade(self):
        prof_esq = 0
        if self.left:
            prof_esq = self.left.profundidade()
        prof_dir = 0
        if self.right:
            prof_dir = self.right.profundidade()
        return 1 + max(prof_esq, prof_dir)

    def inserir(self, novo):
        no = No(novo)
        if self.root == None:
            self.root = no
            return 'Foi adicionado com sucesso !'

        else:
            atual = self.root
            while atual != None:
                ant = atual
                if novo.get_id() < atual.dado.get_id():  # indo p/ esquerda
                    atual = atual.left
                    if atual == None:
                        ant.left = no
                elif novo.get_id() > atual.dado.get_id():  # indo p/ direita
                    atual = atual.right
                    if atual == None:
                        ant.right = no
                else:
                    return f'O ID {novo.get_id()} já existe !'
            return 'Foi adicionado com sucesso !'

    def buscaid(self, ide):
        if self.root == None:
            print('Arvore Vazia')
        else:
            atual = self.root
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
        if self.root == None:
            print('Arvore Vazia')
        else:
            atual = self.root
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

    def altura(self, atual):  # atual = root, ta na entrada
        if atual == None:
            return -1
        elif atual.left == None and atual.right == None:
            return 0
        else:
            if self.altura(atual.left) > self.altura(atual.right):
                return self.altura(atual.left) + 1
            else:
                return self.altura(atual.right) + 1
    def balanceado(self):
        profundidaesq = 0
        if self.left:
            profundidaesq = self.left.profundidade
        profundidadedir = 0
        if self.right:
            profundidadedir = self.right.profundidade
        return  profundidaesq, profundidadedir

    def emordem(self, atual):  # atual = root, ta na entrada !
        if atual != None:
            self.emordem(atual.left)
            print(f'chave: {atual.dado.get_id()}')
            self.emordem(atual.right)

    def rotacaoEsquerda(self):
        self.dado, self.right.dado = self.right.dado, self.dado
        old_left= self.left
        self.setaFilhos(self.right, self.right.right)
        self.left.setaFilhos(old_left, self.left.left)

    def rotacaoDireita(self):
        self.dado, self.left.dado = self.left.dado, self.dado
        old_right = self.right
        self.setaFilhos(self.left.left, self.left)
        self.right.setaFilhos(self.right.right, old_right)

    def rotacaoEsquerdaDireita(self):
        self.left.rotacaoEsquerda()
        self.rotacaoDireita()

    def rotacaoDireitaEsquerda(self):
        self.right.rotacaoDireita()
        self.rotacaoEsquerda()

    def executaBalanco(self):
        bal = self.balanceado()
        if bal > 1:
            if self.left.balanco() > 0:
                self.rotacaoDireita()
            else:
                self.rotacaoEsquerdaDireita()
        elif bal < -1:
            if self.right.balanco() < 0:
                self.rotacaoEsquerda()
            else:
                self.rotacaoDireitaEsquerda()

    def inOrder(self, atual):
        if atual != None:
            self.inOrder(atual.left)
            print(atual.dado, end=" ")
            self.inOrder(atual.right)
    def caminhar(self):
        print(" Exibindo em ordem: ", end="")
        self.inOrder(self.root)
    def __str__(self):
        return str(self.dado)

    def menu(self):
        return input(""" 
0) sair do Menu
1) Inserir filme
2) Buscar filme pelo id    
3) Buscar filmes pelo ano  
4) Listar filmes em ordem alfabética 
5) Altura da árvore 
6) Exibir a árvore
Digite sua opção: 
""")


arv = avl()
resp = arv.menu()
while resp != '0':
    if resp == '1':
        filme = input('Filme: ')
        ano = int(input('Ano: '))
        chave = int(input('Chave: '))
        novo = Dado(filme, ano, chave)
        print(arv.inserir(novo))
    if resp == '2':
        chave = int(input('Chave Buscada: '))
        arv.buscaid(chave)
    if resp == '3':
        ano = int(input('Ano Buscado: '))
        arv.buscaano(ano)
    if resp == '4':
        a = None

    if resp == '5':
        print(f'Altura: {arv.altura(arv.root)}')
    if resp == '6':
        arv.caminhar()
    if resp not in ['0', '1', '2', '3', '4', '5', '6']:
        print('Comando invalido')
    resp = arv.menu()
print('Fim')
