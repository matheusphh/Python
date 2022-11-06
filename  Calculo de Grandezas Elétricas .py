#Mateus Cardoso Rocha
##18/06/2022
#Grandezas Eletricas

print('''****************************************
      Calculo de Grandezas Eletricas 

Digite
1 para tensão (Volt)
2 para corrente (Ampére)
3 para resistência (Ohm)
****************************************
Qual grandeza deseja calcular?''')

grand = int(input())

if grand == 1:
    a = int(input("Digite o valor da resistencia: " ))
    b = int(input("Digite o valor da corrente: "))
    result = a * b
    print(result, "volts")

if grand == 2:
    a = int(input("Digite o valor da tensão: "))
    b = int(input("Digite o valor da resistencia: "))
    result = a / b
    print(result, "amperes")

if grand == 3:
    a = int(input("Digite o valor da tensão: "))
    b = int(input("Digite o valor da corrente: "))
    result = a / b
    print(result, "Ohm")