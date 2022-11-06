#Dispositivo de Briotti Ruffini

print("Digite os 4 termos da equação do terceiro grau.")

x = -100
y = 0
a = int(input(print("ax³: ")))
b = int(input(print("bx²: ")))
c = int(input(print("cx: ")))
d = int(input(print("d: ")))
print()

print("A sua equação é:")
print(a,"x³ + ", b,"x² +", c,"x +", d)
print()


raiz = (a*(x**3))+(b*(x**2))+(c*x)+d

while (raiz != 0) and (x < 100):
    x = x + 1 
    raiz = (a*(x**3))+(b*(x**2))+(c*x)+d
    if raiz == 0:
         raiz = (a*(x**3))+(b*(x**2))+(c*x)+d
         y = x
         print(y, "É uma raiz!")
         print()
         break

######################################################

ax2 = a
ax = (ax2 * y) + b
a =  (ax * y) + c 

print("A equação reduzida é")
print(ax2,"x² + ", ax,"x +", a)