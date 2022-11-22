import sqlite3
mydb = sqlite3.connect("supermarket.db")
mycursor = mydb.cursor()


def verifica_login(username, password):
    sqlFormula = f"SELECT * FROM users WHERE username='{username}'"
    mycursor.execute(sqlFormula)
    query = mycursor.fetchall()
    if (len(query) > 0 and query[0][1] == password):
        return { 'status': 'success', 'message': 'Login realizado com sucesso.'}
    else:
        return { 'status': 'error', 'message': 'Usuário ou senha inválidos.' }


def cadastro_login(username, password):
    sqlFormula = f"SELECT * FROM users WHERE username='{username}'"
    mycursor.execute(sqlFormula)
    query = mycursor.fetchall()

    if (len(query) > 0):
        return { 'status': 'error', 'message': 'Usuário já existente.'}
    else:
        sqlFormula = f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')"
        mycursor.execute(sqlFormula)
        mydb.commit()
        return { 'status': 'success', 'message': 'Cadastro realizado com sucesso.'}
