from tkinter import*
from ArvoreAVL import No
from Dados import Dado
root = Tk()
arv = No()
listachaves = []
listaanos = []
listafilmes = []
listaD = []
root.title("Projeto Árvore AVL")
root.geometry("280x200+600+250")
def inserirFilme():
    top = Toplevel()
    top.geometry("300x200+500+300")
    top.title('INSERIR')
    nome_Filme = Label(top, text="Filme:  ")
    nome_Filme.pack()
    entrada1 = Entry(top)
    entrada1.pack()
    nome_Ano = Label(top,text ="Ano: ")
    nome_Ano.pack()
    entrada2 = Entry(top)
    entrada2.pack()
    nome_Chave = Label(top,text="Chave: ")
    nome_Chave.pack()
    entrada3 = Entry(top)
    entrada3.pack()
    botao_add = Button(top,text="Adicionar", command= arv.inserir(No(Dado(entrada1.get(), entrada2.get()), entrada3.get()),'ext'))
    botao_add.pack()

def buscarFilmeId():
    top = Toplevel()
    top.geometry("400x100+500+300")
    top.title('BUSCAR ID')
    nome_Filme = Label(top, text="Id do filme que você procura:  ")
    nome_Filme.pack()
    id = Entry(top)
    id.pack()
    botao_Procura = Button(top,text="Buscar Filme pelo ID", command = text3.configure(arv.buscaid(id.get(), listachaves, listaD)))
    botao_Procura.pack()

def buscarFilmeAno():
    top = Toplevel()
    top.geometry("400x100+500+300")
    top.title('BUSCAR ANO')
    nome_Filme = Label(top, text="Ano do filme que você procura:  ")
    nome_Filme.pack()
    ano = Entry(top)
    ano.pack()
    botao_Procura_ano = Button(top, text="Buscar Filme pelo Ano", command = text3.configure((arv.buscaano(ano.get(), listachaves, listaD))))
    botao_Procura_ano.pack()

def ordemAlfa():
    text3.configure(text= arv.OrdemAlfa(listafilmes))
def Altura():
    text3.configure(text= arv.altura())
def exibir():
    text3.configure(text=arv.print())
botao_sair = Button(text = "Sair", command = quit, width = 15)
botao_sair.grid(column = 0, row = 1, padx = 10, pady = 5)

botao_inserir = Button(root, text = "Inserir", command = inserirFilme, width = 15)
botao_inserir.grid(column = 1, row = 1, padx = 10, pady = 5)

botao_buscarId = Button(text = "Buscar pelo Id", command = buscarFilmeId,width = 15)
botao_buscarId.grid(column = 0, row = 2, padx = 10, pady = 5 )

botao_buscarAno = Button(text = "Buscar pelo Ano", command = buscarFilmeAno, width = 15)
botao_buscarAno.grid(column = 1, row = 2, padx = 10, pady = 5 )

botao_ordemAlfa = Button(text = "Ordem Alfabética", command = ordemAlfa, width = 15)
botao_ordemAlfa.grid(column = 0, row = 3, padx = 10, pady = 5 )

botao_altura = Button(text = "Altura", command = Altura, width = 15)
botao_altura.grid(column = 1, row = 3, padx = 10, pady = 5 )

botao_exibir = Button(text = "Exibir Árvore", command = exibir, width = 15)
botao_exibir.grid(column = 0, row = 4, padx = 10, pady = 5 )


text2 = Label(text = 'Exibição: ')
text2.grid(column = 1, row = 4)

text3 = Label(text = '')
text3.grid(column = 1, row = 5)



root.mainloop()
