from modulo_de_alteracao import *
from tkinter import *


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
  
  
