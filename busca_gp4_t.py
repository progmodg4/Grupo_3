import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from functools import partial
con = sqlite3.connect(r"supermarket_TEST.db")  


def busca_nome(nome, BancoDados):

    con = sqlite3.connect("supermarket.db")
    cursor = con.cursor()

    try:
        cursor.execute(f'''SELECT * FROM {BancoDados} WHERE Nome_do_produto  = {f"'{nome}'"}''')
        #faz a busca em sql
    except:
        return None

    rows = cursor.fetchall()
    #pega o resultado do select
    for row in rows:
        return row

def busca_numero(numero, BancoDados):

    con = sqlite3.connect("supermarket.db")
    cursor = con.cursor()

    try:
        cursor.execute(f'''SELECT * FROM {BancoDados} WHERE Numero_do_produto  = {f"'{numero}'"}''')
        #faz a busca em sql
    except:
        return None

    rows = cursor.fetchall()
    #pega o resultado do select
    for row in rows:
        return row
