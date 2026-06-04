#LISTAS: Las listas son ordenadas, modificadas, modificables y permiten valores duplicados

# Índices:    0          1           2           3
# frutas = ["Manzana", "Naranja", "Mandarina", "Naranja"]
# print(frutas)
# print(type(frutas))

# frutas [1] = "Banana" #Sobre escribimos la posicion 1

# print(frutas[1]) # Del indice toma "Naranja"


# print("-----------------------------------------------")

# lista = ["Matman1584", 5, True]
# print(lista)
# print(type(lista))

# print(len(lista))

# print(frutas[0:2])
# print(frutas[:3])
# print(frutas[2:])

# if "Manzana" in frutas:
#     print("La Manzana esta dentro de las frutas")

# Indice        0       1        2
vehiculos = ["Carro", "Moto", "Avion"]

# # Metodos
# # APPEND (Agregar un elemento al final de una lista)
# vehiculos.append("Barco") # Indice 3

# # INSERT
# vehiculos.insert(1, "Bicicleta")
# print(vehiculos)

# # REMOVE
# vehiculos.remove("Carro")
# print(vehiculos)

# #POP
# vehiculos.pop(1) # Elimina al elemento Moto ubicado indice 1
# print(vehiculos)

# # SORT
# vehiculos.sort()
# print(vehiculos)

# #INVERSE
# vehiculos.reverse()
# print(vehiculos)

# UNIR LISTAS
coleccion1 = [1, 2, 3]
coleccion2 = [4, 5 , 6]

coleccion3 = coleccion1 + coleccion2
print(coleccion3)

coleccion1.extend(coleccion2)
print(coleccion1)