#Este es importante para el desarrollo de videojuego, el control de flujo es la decision que toma python cuando se cumple o no la condicion.

if 10 > 9:
    print("Es correcto")

if False:
    print("Es correcto")

else:
    print("No es correcto")

mascota = 'perro'

if mascota == 'gato':
    print("Tienes un gato")
elif mascota == 'perro':
    print("Tienes un perro")
else:
    print("No se que animal tienes")


edad = 16
calificacion = 9

if edad < 18:
    print("Eres menor de edad")
    if calificacion >= 7:
        print("Aprobado")
    else:
        print("No Aprobado")

else:
    print("Eres adulto")



num1 = int(input("Ingresa un número:"))
num2 = int(input("Ingresa otro número:"))

f"{num1} es mayor que {num2}"
"num2 es mayor que num1"
"num1 y num2 son iguales"

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
else:
    print(f"{num1} y {num2} son iguales")


edad1 = 16
tiene_licencia = False


if edad1 >= 18 and tiene_licencia:
    print("Puedes conducir")
elif edad1 < 18 and not tiene_licencia:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")
elif edad1 >= 18 and not tiene_licencia:
    print("No puedes conducir. Necesitas contar con una licencia")