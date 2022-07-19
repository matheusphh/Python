cap = int(input("Capital: "))
porc = int(input('Porcentgem: '))
cont = 1

calc = porc / 100
while cont < 17:
    print('$', cap * calc)
    cont += 1


