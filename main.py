from sys import exit
from random import randint
from __init__.funcion1 import *
from __init__.funcion2 import *
from __init__.setting import *

print()
print(format("BIENVENIDO","-^75"))
print(format("ADIVINE EL NUMERO","-^75"))
print()
texto = setText()
rango1, rango2 = setRango()
numero_aleatorio = randint(rango1, rango2)
print(f"Sus rangos son: {rango1} al {rango2}")

while INTENTOS > 0:
    print(f"Intentos Restantes: {INTENTOS}")
    try:
        numero = int(input(f"{texto}"))
    except ValueError:
        print("Error: Tiene que ser un numero")

    if numero_aleatorio < numero and INTENTOS != 1:
        print("Demasiado Grande")
        INTENTOS -= 1
    elif numero_aleatorio > numero and INTENTOS != 1:
        print("Demasiado Pequeño")
        INTENTOS -= 1
    elif numero == numero_aleatorio:
        print(f"Has Ganado en el {INTENTOS} intento")
        input("Pulse enter para continuar...")
        exit()
    elif numero != numero_aleatorio and INTENTOS == 1:
        print()
        print(format("GAME OVER","-^75"))
        INTENTOS -= 1
        input("Pulse enter para continuar...")
        exit()
