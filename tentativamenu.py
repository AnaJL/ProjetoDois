from tkinter import *
from Dados import *
from Node import  *
def button1_click():
    filme = ed1.get()
    ano = ed2.get()
    Dado(filme,ano)
    lb["text"] = "Inserido com sucesso!"
def button2_click():
    print("bt_click")
janela = Tk() #Cria a janela
ed1 = Entry(janela)
ed1.place(x = 300, y =100)
ed2 = Entry(janela)
ed2.place(x = 300, y =150)
ed3 = Entry(janela)
ed3.place(x = 300, y =200)
ed4 = Entry(janela)
ed4.place(x = 300, y =250)
janela.title("Árvore AVL")
janela["bg"] = "gray"
bt1 = Button(janela, width = 20, text = "Inserir filme", command = button1_click)
bt1.place(x = 100, y = 100)
bt2 = Button(janela, width = 20, text = "Buscar filme pelo id  ", command = button1_click)
bt2.place(x = 100, y = 150)
bt3 = Button(janela, width = 20, text = "Buscar filmes pelo ano ", command = button1_click)
bt3.place(x = 100, y = 200)
bt4 = Button(janela, width = 20, text = "sair do Menu", command = quit)
bt4.place(x = 100, y = 250)
lb = Label(janela, text = "A Resposta irá aparecer aqui!")
lb.place(x=200, y= 50)
#largura x Altura + Esquerda do vídeo+ Topo do vídeo
janela.geometry("600x400+400+100")
janela.mainloop() #Laço de repetição enquanto a janela está aberta
