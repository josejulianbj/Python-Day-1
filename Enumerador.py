lista = ['a','b','c']
indice = 0

for item in lista:
    print(indice,item)
    indice += 1

#Aqui aplicamos el enumaerador, es mas sintetico.

lista2 = ['a','b','c']

for indice,item in enumerate(lista2):
    print(indice,item)


for indice,item in enumerate(range(50,55)):
    print(indice,item)

my_tuples = list(enumerate(lista))
print(my_tuples)
