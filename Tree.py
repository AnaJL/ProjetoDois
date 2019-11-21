from Node import No
from Dados import Dado

class avl:
    def __init__(self, dado = None):
            self._root = dado
    def inserir(self, novo):
        no = No(novo)
        if self._root == None:
            self._root = no
            return 'Foi adicionado com sucesso !'
        
        else:
            atual = self._root
            while atual != None:
                ant = atual
                if novo.get_id() < atual.dado.get_id(): #indo p/ esquerda
                    atual = atual.left
                    if atual == None:
                        ant.left = no
                elif novo.get_id() > atual.dado.get_id():                                  #indo p/ direita
                    atual = atual.right
                    if atual == None:
                        ant.right = no
                else:
                    return f'O ID {novo.get_id()} já existe !'
            return 'Foi adicionado com sucesso !'
            
    def buscaid(self, ide):
        if self._root == None:
            print('Arvore Vazia')
        else:
            atual = self._root
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
        if self._root == None:
            print('Arvore Vazia')
        else:
            atual = self._root
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

        
    def altura(self, atual):  #atual = root, ta na entrada
        if atual == None:
            return -1
        elif atual.left == None and atual.right == None:
            return 0
        else:
            if self.altura(atual.left) > self.altura(atual.right):
                return self.altura(atual.left) + 1
            else:
                return self.altura(atual.right) + 1

    def emordem(self, atual): #atual = root, ta na entrada !
        if atual != None:
            self.emordem(atual.left)
            print(f'chave: {atual.dado.get_id()}')
            self.emordem(atual.right)
                    
    def __str__(self):
        return str(self._dado)
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
    if resp == '1' :
        filme = input('Filme: ')
        ano = int(input('Ano: '))
        chave = int(input('Chave: '))
        novo = Dado(filme, ano, chave)
        print(arv.inserir(novo))
    if resp == '2' :
        chave = int(input('Chave Buscada: '))
        arv.buscaid(chave)
    if resp == '3' :
        ano = int(input('Ano Buscado: '))
        arv.buscaano(ano)
    if resp == '4' :
        a = None
        print(arv.OrdemAlfa(a))
    if resp == '5' :
        print(f'Altura: {arv.altura(arv._root)}')
    if resp == '6' :
        arv.emordem(arv._root)
    if resp not in ['0','1','2','3','4','5','6']:
        print('Comando invalido')
    resp = arv.menu()
print('Fim')


