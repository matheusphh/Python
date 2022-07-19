seg = 0
hor = int(input("Qual é a hora? "))
min = int(input("Qual o minuto? "))

import time

print()

while hor < 25:    
    while min < 60:
        while seg < 60:
            print(hor, ":", min, ":", seg)
            time.sleep(1)
            seg += 1
            if seg == 60:
                min += 1
                seg = 00
                if min == 60:
                    hor += 1
                    min = 0
                    if hor == 24:
                        hor = 0
                        min = 0
                        min = 0
                        
                
