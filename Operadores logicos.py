#Operadores logicos son 'y', 'o' y 'no', 'and','or' y 'not'

mi_bool = (4 < 5) and (5 > 6) #En este se tienen que cumplir todas las condiciones para que de True, si una no se cumple automaticamente da falso.
print(mi_bool)

mi_bool_2 = (4 < 5) and (5 < 6) #En este se tienen que cumplir todas las condiciones para que de True, si una no se cumple automaticamente da falso.
print(mi_bool_2)

mi_bool_3 = (55==55) and ('perro'=='perro')
print(mi_bool_3)

mi_bool_4 = 10 == 10 or 3==3 #En este se tiene que cumplir una de todas las condiciones, ninguna se cumple pues dara falso, si una sola se cumple da verdadero.
print(mi_bool_4)

mi_bool_5 = 10 == 11 or 3==4
print(mi_bool_5)

texto = 'Esta frase es breve'

mi_bool_6 = 'frase' in texto
print(mi_bool_6)


texto2 = 'Esta frase es breve'

mi_bool_7 = ('frase' in texto) or ('python' in texto)
print(mi_bool_7)

#not

mi_bool_8 = not 'a' == 'a' #Este cambia la comparacion, es decir aunque sea verdadera, el not cambia eso y la vuelve falsa. lo mismo al revez
print(mi_bool_8)

mi_bool_9 = not 'a' != 'a' #Recordemos que != es 'DIFERENTE' por lo tanto aqui buscamos como una doble negacion y eso nos da Verdadero.
print(mi_bool_9)

frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"

mi_bool_10 = palabra1 not in frase and palabra2 not in frase
print(mi_bool_10)