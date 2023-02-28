#Segundos para horas

seg = int(input(print("Digite os segundos para convertevos em horas: ")))


minutos = 0
horas = 0

while seg > 59:
    minutos += 1
    if minutos == 60:
        horas += 1
        minutos -= 60
    seg -= 60



print(horas,":", minutos, ":", seg)








