#Calculadora de IMC
#Mateus Cardoso 
#18/06/2022

peso = int(input("Digite o peso do paciente: "))
altu = float(input("Digite a altura do paciente: "))

imc = peso / (altu * altu)

print("O IMC desse paciente é: ", + imc)

if imc < 18.5:
    print("Abaixo do peso!")

if (imc > 18.5) and (imc < 25):
    print("Peso Normal")

if (imc >= 25) and (imc < 30):
    print("Sobrepeso")

if (imc >= 30) and (imc < 35):
    print("Obesidade grau 1")

if (imc >= 35) and (imc < 40):
    print("Obesidade grau 2")

if (imc >= 40):
    print("Obesidade grau 3")