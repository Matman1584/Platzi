#  TUPLA: Colección ordenada e inmutable de elementos que permiten duplicados

#Indice           0            1        2
# tecnologias = ("Python", "JavaScript", "Go")

# print(tecnologias) # Imprime todos los elementos de la tupla
# print(tecnologias[1])

# # Contar cuantos elementos hay en una tupla
# print(len(tecnologias))

# # Ver qué tipo de variable es
# print(type(tecnologias))

# # La coma especifica que es una tupla
# fruta = ("Manzana",)
# print(type(fruta))

# #TUPLA con diferentes elementos
# tupla = ("Python", 5, True)
# print(tupla)

# x, y, z = tupla
# print(x)
# print(y)
# print(z)


# Concatenar tuplas
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

tupla3 = tupla1 + tupla2 # Se crea una tercera tupla que las suma
print(tupla3)

tupla = ("Python", 5, True)

print(tupla * 2)

print("-------------------------------------------")


tuplaAModificar = ("Python", "JavaScript", "Go")
tuplaConvertidaEnLista = list(tuplaAModificar)
tuplaConvertidaEnLista += ["Loro", "Pez"] # += hace los mismo que append
tuplaAModificar = tuple(tuplaConvertidaEnLista)
print(tuplaAModificar)
