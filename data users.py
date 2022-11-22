import sqlite3
from sqlite3 import Error


con = sqlite3.connect(r"supermarket.db") 
cursor = con.cursor()
cursor.execute(f"""CREATE TABLE "users" (
  "username" VARCHAR(45) NOT NULL,
  "password" VARCHAR(45) NOT NULL,
  PRIMARY KEY ("username"));""") #insere as variáveis
con.commit() #dá commit na mudança
