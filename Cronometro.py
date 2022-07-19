min = 0
seg = 0

import time

minFinal = int(input("Quandos minutos deseja? "))

while minFinal > min:
    print(min, ":", seg)
    time.sleep(1)
    seg += 1
    if seg == 60:
        min += 1
        seg = 0

    