import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from functools import partial
con = sqlite3.connect("supermarket.db") 
cursor = con.cursor()

def insere(): 
    global entry
    global entry2
    global entry3
    global entry4
    nome = entry.get()
    quantidade = entry2.get()
    preco = entry3.get()
    num = entry4.get()
    cursor.execute(f"INSERT INTO Supermercado (Numero_do_produto,Nome_do_produto,Quantidade_do_produto,Preco_do_produto) VALUES ('{num}','{nome}','{quantidade}','{preco}')")
    con.commit()
  

def remove():
    global entry4
    num = entry4.get()
    sql = "DELETE FROM Supermercado WHERE Numero_do_produto = ?"
    cursor.execute(sql, (num,))
    con.commit()

def atualiza_nome():
    global entry
    global entry4
    nome = entry.get()
    num = entry4.get()
    sql = "UPDATE Supermercado SET Nome_do_produto = ? WHERE Numero_do_produto = ?"
    cursor.execute(sql, (nome,num,))
    con.commit()

def atualiza_qtd():
    global entry2
    global entry4
    qtd = entry2.get()
    num = entry4.get()
    sql = "UPDATE Supermercado SET Quantidade_do_produto = ? WHERE Numero_do_produto = ?"
    cursor.execute(sql, (qtd,num,))
    con.commit()

def atualiza_preco():
    global entry3
    global entry4
    preco = entry3.get()
    num = entry4.get()
    sql = "UPDATE Supermercado SET Preco_do_produto = ? WHERE Numero_do_produto = ?"
    cursor.execute(sql, (preco,num,))
    con.commit()

    
    
def novajanela():
    global entry
    global entry2
    global entry3
    global entry4
    win = Toplevel(janela)
    win.title("insercao")
    win.geometry("250x200")
    txt4 = Label(win,text = "Número do produto")
    txt4.grid(column = 0, row = 0)
    entry4 = Entry(win,width = 40)
    entry4.focus_set()
    entry4.grid(column = 0, row = 3)
    txt = Label(win,text = "Nome")
    txt.grid(column = 0, row = 6)
    entry = Entry(win,width = 40)
    entry.focus_set()
    entry.grid(column = 0, row = 9)
    txt2 = Label(win,text = "quantidade")
    txt2.grid(column = 0, row = 12)
    entry2 = Entry(win,width = 40)
    entry2.focus_set()
    entry2.grid(column = 0, row = 15)
    txt3 = Label(win,text = "Preco") 
    txt3.grid(column = 0, row = 18)
    entry3 = Entry(win,width = 40)
    entry3.focus_set()
    entry3.grid(column = 0, row = 21)
    btn = Button(win,text = "inserir", command = partial(insere))
    btn.grid(column=0,row = 24)

def updatejanela():
    global entry
    global entry2
    global entry3
    global entry4
    num = entry4.get()
    win = Toplevel(janela)
    win.title("Atualização")
    win.geometry("250x200")
    txt = Label(win,text = "Nome")
    txt.grid(column = 0, row = 0)
    entry = Entry(win,width = 40)
    entry.focus_set()
    entry.grid(column = 0, row = 3)
    btn_name = Button(win,text = "Atualiza nome", command = partial(atualiza_nome))
    btn_name.grid(column=0,row = 6)
    txt2 = Label(win,text = "quantidade")
    txt2.grid(column = 0, row = 9)
    entry2 = Entry(win,width = 40)
    entry2.focus_set()
    entry2.grid(column = 0, row = 12)
    btn_name = Button(win,text = "Atualiza quantidade", command = partial(atualiza_qtd))
    btn_name.grid(column=0,row = 15)
    txt3 = Label(win,text = "Preco") 
    txt3.grid(column = 0, row = 18)
    entry3 = Entry(win,width = 40)
    entry3.focus_set()
    entry3.grid(column = 0, row = 21)
    btn_preco = Button(win,text = "Atualiza preço", command = partial(atualiza_preco))
    btn_preco.grid(column=0,row = 24)
    
def retirarjanela():
    global entry4
    win = Toplevel(janela)
    win.title("remoção")
    win.geometry("250x200")
    txt = Label(win,text = "Insira o número do produto que deseja remover")
    txt.grid(column = 0, row = 0)
    entry4 = Entry(win,width = 40)
    entry4.focus_set()
    entry4.grid(column = 0, row = 3)
    btn = Button(win,text = "Remover", command = partial(remove))
    btn.grid(column=0,row = 18)
    
def atualizajanela():
    global entry4
    win = Toplevel(janela)
    win.title("Atualiza")
    win.geometry("250x200")
    txt = Label(win,text = "Insira o número do produto que deseja atualizar")
    txt.grid(column = 0, row = 0)
    entry4 = Entry(win,width = 40)
    entry4.focus_set()
    entry4.grid(column=0,row = 3)
    btnok = Button(win, text= "OK",command = updatejanela)
    btnok.grid(column = 0, row = 6)

def printa_row():
    global entry4
    num = entry4.get()
    sql = "SELECT * FROM Supermercado WHERE Numero_do_produto = ?"
    desejado = cursor.execute(sql,(num,))
    win = Toplevel(janela)
    win.title("Produto")
    win.geometry("250x60")
    i = 0
    for Supermercado in desejado:
        for j in range(len(Supermercado)):
            e = Label(win,width = 200,fg = 'blue',text = Supermercado,anchor = 'w')
            e.grid(row = 1, column = i)

def printa_row2():
    global entry2
    nome = entry2.get()
    sql = "SELECT * FROM Supermercado WHERE Nome_do_produto = ?"
    desejado = cursor.execute(sql,(nome,))
    win = Toplevel(janela)
    win.title("Produto")
    win.geometry("250x60")
    i = 0
    for Supermercado in desejado:
        for j in range(len(Supermercado)):
            e = Label(win,width = 200,fg = 'blue',text = Supermercado,anchor = 'w')
            e.grid(row = 1, column = i)
            
def buscajanela():
    global entry4
    global entry2
    win = Toplevel(janela)
    win.title("Busca")
    win.geometry("400x200")
    txt = Label(win,text = "Número")
    txt.grid(column = 0, row = 0)
    entry4 = Entry(win,width = 40)
    entry4.focus_set()
    entry4.grid(column = 0, row = 3)
    btn_name = Button(win,text = "Buscar por número", command = partial(printa_row))
    btn_name.grid(column=0,row = 6)
    txt = Label(win,text = "Nome")
    txt.grid(column = 0, row = 9)
    entry2 = Entry(win,width = 40)
    entry2.focus_set()
    entry2.grid(column = 0, row = 12)
    btn_name = Button(win,text = "Buscar por nome", command = partial(printa_row2))
    btn_name.grid(column=0,row = 15)
    



entry = ' '
entry2 = 0
entry3 = 0
entry4 = 0
janela = Tk()
janela.title("Stockdata")
texto_orientacao = Label(janela, text = "Botão inserir:Insere um novo produto no banco de dados\nBotão remover:Retira produto do banco de dados\nBotão alterar:Escolha um produto e insira qualquer alteração em seu estoque\nBotão busca:procura um produto\n")
texto_orientacao.grid(column = 0, row = 0)
botao1 = Button(janela, text = "Inserir", command = novajanela)
botao1.grid(column = 0, row = 3)
botao2 = Button(janela, text = "Retirar", command = retirarjanela)
botao2.grid(column = 0, row = 5)
botao3 = Button(janela, text = "Alterar",command = atualizajanela)
botao3.grid(column = 0, row = 7)
botao4 = Button(janela, text = "Busca",command = buscajanela)
botao4.grid(column = 0, row = 9)

janela.mainloop()



# inserção                                          

# sele
#con.commit()    
