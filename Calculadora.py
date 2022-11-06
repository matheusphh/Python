#Operações Matemáticas
#Mateus Cardoso Rocha
#18/06/2022

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

calc=0
while calc != 4:
    calc = int(input("Escola uma das opcões: 1(+) 2(-) 3(x) 4(/): ")) 
    if calc == 1:
        result = (num1 + num2)
        print("O resultado é :", result)


    if calc == 2:
        result = (num1 - num2)
        print("O resultado é :", result)

    if calc == 3:
        result = (num1 * num2)
        print("O resultado é :", result)

    if  calc == 4:
        result = (num1 / num2)
        print("O resultado é :", result)

