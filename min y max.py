menor = min(58,96,72,64,35)
print(menor)

mayor = max(58,96,72,64,35)
print(mayor)

lista = [58,96,72,64,35]
print(max(lista))

lista = [58,96,72,64,35]
print(lista)
print(f'El menor es {min(lista)} y el mayor es {max(lista)}')

nombres = ['Juan','Pablo','Alicia','Carlos']

print(min(nombres))

nombre = "Carlos"
print(min(nombre))

nombre2 = "Carlos"
print(min(nombre2.lower()))

dic = {'C1':45,'C2':11}
print(min(dic.values()))

#Utilizando max(), min() y métodos de diccionarios, obtén el mínimo valor a partir del siguiente diccionario:
#diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}
#Almacena dicho valor en una variable llamada edad_minima.
#También, obtén el nombre que se ubica último en orden alfabético, y almacénalo en una variable llamada ultimo_nombre.

#Solucion
diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}

edad_minima = min(diccionario_edades.values())
ultimo_nombre = max(diccionario_edades.keys())