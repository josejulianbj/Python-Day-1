palabra = 'Python'

lista = [letra for letra in palabra]

print(lista)

lista2 = [n/2 for n in range (0,21,2)]

print(lista2)

lista3 = [n for n in range (0,21,2) if n * 2 > 10]

print(lista3)

lista4 = [n if n * 2 > 10 else "No" for n in range (0,21,2)]

print(lista4)

pies = [10,20,30,40,50]
metros = [p / 3.281 for p in pies]

print(metros)