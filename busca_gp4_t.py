import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from functools import partial
con = sqlite3.connect(r"supermarket_TEST.db")  


def busca_nome(nome, BancoDados):
    cursor = con.cursor()
    cursor.execute('SELECT * FROM ' + BancoDados + ' WHERE Nome_do_produto =?', (nome,))
    #faz a busca em sql
    
    rows = cursor.fetchall()
    #pega o resultado do select

    return rows

def busca_numero(numero, BancoDados):
    cursor = con.cursor()
    cursor.execute('SELECT * FROM ' + BancoDados + ' WHERE Numero_do_produto =?', (numero,))
    #faz a busca em sql
    
    rows = cursor.fetchall()
    #pega o resultado do select

    return rows
