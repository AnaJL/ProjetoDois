from tkinter import *
from Dados import *
from Node import  *
from random import randint
def button1_click():
    filme = ed1.get()
    ano = ed2.get()
    chave = randint(1,1000)
    Dado(filme,ano,chave)
    lb["text"] = "Inserido com sucesso!"
def button2_click():
    print("bt_click")
janela = Tk() #Cria a janela
ed1 = Entry(janela)
ed1.place(x = 100, y =100)
ed2 = Entry(janela)
ed2.place(x=100, y= 150)
ed3 = Entry(janela)
ed3.place(x=100,y=200)
janela.title("Árvore AVL")
bt1 = Button(janela, width = 20, text = "Inserir Filme", command = button1_click)
bt1.place(x = 200, y = 250)
lbFilme = Label(janela, text= "Filme: ")
lbFilme.place(x = 50, y=100)
lbAno = Label(janela, text= "Ano: ")
lbAno.place(x=50, y= 150)
lbChave = Label(janela, text="Chave: ")
lbChave.place(x=50, y=200)
lb = Label(janela, text = "A Resposta irá aparecer aqui!")
lb.place(x=200, y= 50)
#largura x Altura + Esquerda do vídeo+ Topo do vídeo
janela.geometry("600x400+400+100")
janela.mainloop() #Laço de repetição enquanto a janela está aberta
