from random import randint

aleatorio = randint(1,50)
print(aleatorio)

from random import *
aleatorio1 = round(uniform(1,5),1)
print(aleatorio1)

colores = ['Azul','Verde','Rojo']
aleatorio3 = choice(colores)
print(aleatorio3)

numeros = list(range(5,50,5))
print(numeros)

shuffle(numeros)
print(numeros)