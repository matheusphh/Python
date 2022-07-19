#Mateus Cardoso Rocha
##18/06/2022
#Grandezas Eletricas

import requests
from tkinter import *

#######################################################

def tencao():
    text11 = Label(janela, text = 'Digite a corrente:')
    text11.grid(column=0, row=3)
    a = int(input("Digite o valor da resistencia: " ))
    b = int(input("Digite o valor da corrente: "))
    result = a * b
    print(result, "volts")

    
def corrente():
    texto2 = Label(janela, text = 'Digite a tenção:')
    texto2.grid(column=0, row=3)
    a = int(input("Digite o valor da tensão: "))
    b = int(input("Digite o valor da resistencia: "))
    result = a / b
    print(result, "amperes")

def resistencia():
    texto3 = Label(janela, text = 'Digite a tenção:')
    texto3.grid(column=0, row=3)
    a = int(input("Digite o valor da tensão: "))
    b = int(input("Digite o valor da coreente: "))
    result = a /b
    print(result, "Ohm")
    
########################################################

janela = Tk()

#Header
janela.title("Calculo de Grandezas")

#Body

texto_orientacao = Label(janela, text = 'Qual grandeza deseja calcular?')

texto_orientacao.grid(column=1, row=0)


botao = Button(janela, text = "Tensão", command=tencao)
botao.grid(column=0, row=1)

botao = Button(janela, text = "Corrente", command=corrente)
botao.grid(column=1, row=1)

botao = Button(janela, text = "Resistencia", command=resistencia)
botao.grid(column=2, row=1)


janela.mainloop()