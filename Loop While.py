monedas = 5

while monedas > 0:
    print(f'tengo {monedas} monedas')
    monedas = monedas - 1 #Cada que aplique el Loop este pierde 1 moneda.
                          #Tambien sirve 'moendas -= 1'
else: print("No tengo mas dinero")


respuesta = 's'
while respuesta == 's':
    respuesta = input("Ingrese su respuesta:(s/n) ")

else:
    print("Gracias")


#respuesta2 = "s"
#while respuesta2 == "s":
#    pass

#print("Hola")


nombre = input("Ingrese su nombre: ") #En este codigo cuando se encuentre con la letra "r" interrumpira el codigo

for letra in nombre:
    if letra == "r":
        break
    print(letra)

nombre2 = input("Ingrese su nombre: ") #saltaremos la letra "r" osea esta se evita.

for letra1 in nombre2:
    if letra1 == "r":
        continue
    print(letra1)