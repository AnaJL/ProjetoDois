from tkinter import*
from Dados import Dado
from Tree import Avl
from Node import No
from random import randint

root = Tk()
root.title("Projeto Árvore AVL")
arv = Avl(No(Dado()))

def emordem():
    a = arv.emordem(arv.root)
    if(a == 'None'):
        text2.configure(text = a)
    else:
        text2.configure(text = a)
def altura():
    if(arv.altura(arv.root) == 0):
        text2.configure(text = '0')
    else:
        text2.configure(text = str(arv.altura(arv.root)))
def inserir():
    chave = randint(0,10000)
    text_chave.configure(text= "sua chave é: ")
    text_chave1.configure(text=chave)
    if (inp.get() == ""):
        text2.configure(text = 'você não colocou filme')
    elif (inp2.get() == ""):
        text2.configure(text = 'você não colocou ano!')
    else:
        a = arv.inserir(No(Dado(inp.get(), inp2.get(),chave)))
        text2.configure(text = a)
def alfabeto():
    text2.configure(text = "a")

text_inp = Label(text = "Filme: ")
text_inp.grid(column = 1, row = 3)
text_fila = Label(text = "Ano: ")
text_fila.grid(column = 1, row = 4)
text_chave = Label(text = '')
text_chave.grid(column = 1, row =5 )
text_chave1 = Label(text = '')
text_chave1.grid(column = 2, row =5 )


inp = Entry()
inp.grid(column = 2, row = 3)
inp2 = Entry()
inp2.grid(column = 2, row = 4)


text2 = Label(text = '')
text2.grid(column = 3, row = 4)

ordem = Button(text = "Em Ordem", command = emordem, width = 15)
ordem.grid(column = 0, row = 4, padx = 10, pady = 5)

altura = Button(text = "Altura", command = altura, width = 15)
altura.grid(column = 0, row = 3, padx = 10, pady = 5)


inserir = Button(text = "Inserir", command = inserir, width = 15)
inserir.grid(column = 3, row = 10, padx = 10, pady = 5)

ordenar = Button(text = "Ordem Alfabetica", command = alfabeto, width = 15)
ordenar.grid(column = 0, row = 5, padx = 10, pady = 5)



root.mainloop()
