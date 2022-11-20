import sqlite3
from sqlite3 import Error


con = sqlite3.connect(r"C:\Users\Usuario\Grupo_3\supermarket.db") 
cursor = con.cursor()
cursor.execute(f"""CREATE TABLE "Supermercado" ("Numero_do_produto"    INTEGER UNIQUE,"Nome_do_produto"    TEXT UNIQUE,"Quantidade_do_produto"    INTEGER,"Preco_do_produto"    NUMERIC,PRIMARY KEY("Numero_do_produto"));""") #insere as variáveis
con.commit() #dá commit na mudança

