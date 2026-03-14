#Un loop es cuando se detecta y se repite

Nombres = ['Juan','Ana','Carlos','Belen','Fran']

#Por cada elemento en Nombres imprimir 'Hola'.

for elemento in Nombres:
    print('Hola ' +  elemento)

lista = ['a','b','c']

for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f'letra {numero_letra}: {letra}')


lista1 = ['pablo','juan','alberto','ryan','luis','laura']
for nombre in lista1:
    if nombre.startswith('l'):
        print(nombre)
    else:
        print('nombre que no comienza con L')

numeros = [1,2,3,4,5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero

    print(mi_valor) #Aqui muestra que se suma cada uno a la vez.
print(mi_valor)     #Aqui muestra el resultado final de la suma.


palabra = 'python es genial '

for letra2 in palabra:
    print(letra2)



for letra3 in 'python':
    print(letra3)

for objeto1 in [[1, 2], [3, 4], [5, 6]]:
    print(objeto1)
    
for a,b in [[1, 2], [3, 4], [5, 6]]:
    print(a)
    print(b)


dic = {'clave1' : 'a','clave2' : 'b','clave3' : 'c'}

for item in dic.items(): #Aqui existen 3 opciones 'dic', 'dic.items','dic.values'
    print(item)


#Este ejercicio es sumar pares e impares por separado
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0

for num in lista_numeros:
    if num % 2 == 0:   # número par
        suma_pares += num
    else:              # número impar
        suma_impares += num

print("Suma de pares:", suma_pares)
print("Suma de impares:", suma_impares)