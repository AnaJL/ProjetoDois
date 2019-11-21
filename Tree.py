from Node import No
from Dados import Dado

class avl:
    def __init__(self, dado = None):
            self._root = dado
    def inserir(self, novo):
        no = No(novo)
        atual = self._root
        if self._root == None:
            self._root = no
        elif atual.get_dado.get_id() > no.get_dado().get_id():
            while atual.get_left != None:
                if atual.get_left == None:  #se o filho esquerdo estiver disponivel, o no vai na posição
                atual.set_proximo(no)
                if atual.get_dado.get_id() > no.get_dado().get_id(): #caminhar para esquerda 
                    atual = atual.get_left()

                
    def __str__(self):
        return str(self._dado)
    def menu(self):
        return int(input(""" 
0) sair do Menu
1) Inserir filme
2) Buscar filme pelo id    
3) Buscar filmes pelo ano  
4) Listar filmes em ordem alfabética 
5) Altura da árvore 
6) Exibir a árvore

Digite sua opção: 
"""))
        
          
arv = avl()
resp = arv.menu()
while resp != 0:
    if resp == 1 :
        filme = input('Filme: ')
        ano = int(input('Ano: '))
        chave = int(input('Chave: '))
        novo = Dado(filme, ano, chave)
        arv.inserir(novo)
    if resp == 2 :
        print('Buscar filme pelo id')
    if resp == 3 :
        print('Buscar filmes pelo ano ')
    if resp == 4 :
        print('Listar filmes em ordem alfabética ')
    if resp == 5 :
        print('Altura da árvore ')
    if resp == 6 :
        print('Exibir a árvore')
    if resp > 6:
        print('Invalido')
    resp = arv.menu()
print('Fim')

