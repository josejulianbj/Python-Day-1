nombres = ['Juan','Pablo','Ana']
edades = [25,42,33]
ciudades = ['Bogota','Madrid','Rio']

combinados = list(zip(nombres,edades,ciudades))

print(combinados)

for nombre,edade,ciudade in combinados:
    print(f"{nombre} tiene {edade} anos y vive en {ciudade}")

