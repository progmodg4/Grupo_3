import sqlite3
from sqlite3 import Error
from functools import partial
import global_variables
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from functools import partial
from login_gp1 import *
from busca_gp4_t import *
import global_variables

con = sqlite3.connect(r"supermarket_TEST.db")  
cursor = con.cursor()
#funções para alterar o banco de dados

def insere_aux(num,nome,quantidade,preco):
    try:
        cursor.execute(f"INSERT INTO Supermercado (Numero_do_produto,Nome_do_produto,Quantidade_do_produto,Preco_do_produto) VALUES ('{num}','{nome}','{quantidade}','{preco}')") #insere as variáveis
        con.commit() #dá commit na mudança
        return 0
    except:
        return 1
    
def insere(): #recebe o input
    global entry  
    global entry2 
    global entry3 
    global entry4 
    nome = entry.get() #Recebe o nome pela caixa de texto
    nome = nome.lower() #coloca o nome em letra minúscula para evitar casos como frango e Frango
    quantidade = entry2.get() #Recebe a quantidade pela caixa de texto
    preco = entry3.get() #Recebe o preço pela qtd de texto
    num = entry4.get() #Recebe o número do produto
    r = insere_aux(num,nome,quantidade,preco)

def remove_aux(num):
    if(busca_numero(num,"Supermercado")==[]):
        return 1
    sql = "DELETE FROM Supermercado WHERE Numero_do_produto = ?" #remove do banco de dados o produto com o número dado
    try:
        cursor.execute(sql, (num,)) 
        con.commit()
        return 0
    except:
        return 1

def remove():#recebe o input
    global entry4
    num = entry4.get() #recebe o número do produto para retirá-lo
    remove_aux(num)
    
def atualiza_nome_aux(num,nome): #faz a alteração do nome com argumentos
    if(busca_numero(num,"Supermercado")==[]):
        return 1
    sql = "UPDATE Supermercado SET Nome_do_produto = ? WHERE Numero_do_produto = ?" #atualiza o nome do produto do número dado
    try:
        cursor.execute(sql, (nome,num,)) 
        con.commit()
        return 0
    except:
        return 1

def atualiza_nome():#recebe o input
    global entry
    global entry4
    nome = entry.get() #Recebe o nome pela caixa de texto
    nome = nome.lower()#coloca o nome em letra minúscula para evitar casos como frango e Frango
    num = entry4.get() #Recebe o número do produto
    atualiza_nome_aux(num,nome)

def atualiza_qtd_aux(num,qtd): #faz a alteração da qtd com argumentos
    if(busca_numero(num,"Supermercado")==[]):
        return 1
    sql = "UPDATE Supermercado SET Quantidade_do_produto = ? WHERE Numero_do_produto = ?" #atualiza o nome do produto do número dado
    try:
        cursor.execute(sql, (qtd,num,)) 
        con.commit()
        return 0
    except:
        return 1

def atualiza_qtd(): #recebe o input
    global entry2
    global entry4
    qtd = entry2.get() #Recebe a qtd pela caixa de texto
    num = entry4.get() #Recebe o número do produto
    atualiza_qtd_aux(num,qtd)

def atualiza_preco_aux(num,preco): #faz a alteração do preço com argumentos
    if(busca_numero(num,"Supermercado")==[]):
        return 1
    sql = "UPDATE Supermercado SET Preco_do_produto = ? WHERE Numero_do_produto = ?"
    try:
        cursor.execute(sql, (preco,num,))
        con.commit()
        return 0
    except:
        return 1

def atualiza_preco():
    global entry3 #Recebe o preço pela caixa de texto
    global entry4 #Recebe o número do produto
    preco = entry3.get()
    num = entry4.get()
    atualiza_preco_aux(num,preco)
### Janelas abaixo são somente para melhor visualização da ferramenta
    
def novajanela():
    global entry
    global entry2
    global entry3
    global entry4
    win = Tk() #abre uma nova janela
    win.title("insercao")
    win.geometry("250x200")
    txt4 = Label(win,text = "Número do produto") #Label para identificar os novos
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

def updatejanela(): #abre janela pra input
    global entry
    global entry2
    global entry3
    global entry4
    global janela
    num = entry4.get() 
    win = Tk() 
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
    
def retirarjanela(): #abre janela pra input
    global entry4
    win = Tk()
    win.title("Remoção")
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
    global janela
    win = Tk()
    win.title("Atualiza")
    win.geometry("250x200")
    txt = Label(win,text = "Insira o número do produto que deseja atualizar")
    txt.grid(column = 0, row = 0)
    entry4 = Entry(win,width = 40)
    entry4.focus_set()
    entry4.grid(column=0,row = 3)
    btnok = Button(win, text= "OK",command = updatejanela)
    btnok.grid(column = 0, row = 6)
### a partir daqui não precisa ser testado

def busca_num(num, BancoDados):
    cursor.execute('SELECT * FROM ' + BancoDados + ' WHERE Numero_do_produto =?', (num,))
    rows = cursor.fetchall()
    for row in rows:
        return row
### a partir daqui não precisa ser testado
    
def printa_row():
    global entry4
    global janela
    num = entry4.get()
    desejado = busca_num(num, "Supermercado")
    win = Tk()
    win.title("Produto")
    win.geometry("250x60")
    i = 0
    for e in desejado:
        e = Label(win,width = 200,fg = 'blue',text = desejado,anchor = 'w')
        e.grid(row = 1, column = i)

def printa_row2():
    global entry
    global janela
    nome = entry.get()
    nome = nome.lower()
    desejado = busca(nome, "Supermercado")
    win = Tk()
    win.title("Produto")
    win.geometry("250x60")
    i = 0
    for e in desejado :
        e = Label(win,width = 200,fg = 'blue',text = desejado,anchor = 'w')
        e.grid(row = 1, column = i)
            
def buscajanela():
    global janela
    global entry4
    global entry
    win = Tk()
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
    entry = Entry(win,width = 40)
    entry.focus_set()
    entry.grid(column = 0, row = 12)
    btn_name = Button(win,text = "Buscar por nome", command = partial(printa_row2))
    btn_name.grid(column=0,row = 15)
    
def menu():
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

def janela_login():
    global entry5
    global entry6
    janela = Tk()
    janela.title("Login")
    texto_user = Label(janela, text = "Usuário:")
    texto_user.grid(column = 0, row = 0)
    entry5 = Entry(janela,width = 40)
    entry5.focus_set()
    entry5.grid(column = 0, row = 3)
    texto_senha = Label(janela, text = "Senha:")
    texto_senha.grid(column = 0, row = 6)
    entry6 = Entry(janela,width = 40)
    entry6.focus_set()
    entry6.grid(column = 0, row = 9)
    botao1 = Button(janela, text = "Inserir", command = verifica_aux)
    botao1.grid(column = 0, row = 12)
    botao_cadastro = Button(janela, text = "Cadastrar", command = cadastro_login_aux)
    botao_cadastro.grid(column = 0, row = 15)

  

def verifica_aux():
    global entry5
    global entry6
    user = entry5.get()
    password = entry6.get()
    result = verifica_login(user,password)
    if(result['status'] == 'success'):
        menu()
        return print("sucesso")
    else:
        return print("falha")

def cadastro_login_aux():
    global entry5
    global entry6
    user = entry5.get()
    password = entry6.get()
    cadastro_login(user,password)
