#Crear un juego de adivinar el numero, intentando que el usuario adivine el numero y cuente el numero de intentos.

from random import randint
from xxsubtype import bench

intentos = 0
estimado = 0
numero_secreto = randint(1,100)

nombre = input("Dime tu nombre: ")

print(f"Bueno {nombre}, eh pensado un numeroi entre 1 y 100\n Tienes 8 intentos para adivinar")

while intentos < 8:
    estimado = int(input("Cual es el numero?: "))
    intentos += 1

    if estimado not in range(1,101):
        print("Tu numero no se encuentra en el rango del 1 y 100")
    if estimado < numero_secreto:
        print("Mi numero es mas alto")
    elif estimado > numero_secreto:
        print("Mi numero es mas bajo")
    else:
        print(f"Felicitaciones {nombre} has adivinado en {intentos} intentos")
        break

if estimado != numero_secreto:
    print(f"Lo siento {nombre} se han agotados los intentos, el numero secreto es {numero_secreto}")