#Terceira Avaliação
#Mateus Cardoso Rocha
#27/07/2022

import random

###############################################################
def Separar(num):
    lista = [0] *5
    for elemento in range(5):
        lista[5 - 1 - elemento] = num % 10
        num = num // 10
    return lista

def contagem(a,b):
    s = set(a)
    return len(s.intersection(b))

def Posicoes_Iguais():
    print ('Sendo',len([index for index, (e1, e2) in enumerate(zip(lista, lista2)) if e1 == e2]), "na posição certa")

###############################################################

print("JOGO DA SENHA")
print("Você tem 5 tentatidas")
print()

semente = int(input("Digite a quantidade de digitos entre 2 e 5: "))
if (semente > 1) and (semente < 6):

    if semente == 2: 
        aleatorio = 99
    if semente == 3:
        aleatorio = 999
    if semente == 4:
        aleatorio = 9999
    if semente == 5:
        aleatorio = 99999

    cont = 1
    num_aleatorio = random.randint(0,aleatorio)
    lista2 = [0] *5
    while cont < 6: 
        print("#######################################")   
        print("Tentativa", cont)
        chute = int(input("Escolha um numero entre 0 e 99.999: "))
        lista = Separar(chute)
        lista2 = Separar(num_aleatorio)
        if (lista == lista2):
            print("/\/\/\/\/\/\/\/")
            print("Você acertou!!!")
            print("\/\/\/\/\/\/\/\ ")
            break
        else:
            print()
            print("Você errou!") 
            print()
            print(contagem(lista,lista2), "numero(os) iguais")
            Posicoes_Iguais()
            print()
            cont += 1
    
    print()
    print("O numero gerado foi: %d"%num_aleatorio)

else:
    print("Numero inválido!")

print("FIM DO PROGRAMA!")

