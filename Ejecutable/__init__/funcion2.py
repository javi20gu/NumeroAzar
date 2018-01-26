from __init__.setting import *

def setRango(num1=POSICION_1, num2=POSICION_2):
    if num1 != POSICION_1 and num2 != POSICION_2:
        print(f"Cambiado rango 1 ---> |{num1}|")
        print(f"Cambiado rango 2 ---> |{num2}|")
        num2 += 1

    elif num2 != POSICION_2:
        print(f"Cambiado rango 2 ---> |{num2}|")
        num2 += 1

    elif num1 != POSICION_1:
        print(f"Cambiado rango 1 ---> |{num1}|")
        num2 += 1
    else:
        num2 += 1
    return num1, num2
