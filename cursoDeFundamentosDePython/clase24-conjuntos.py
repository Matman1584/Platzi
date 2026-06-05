# Conjunto (set): Coleccion no ordenada de elemntos únicos (No se puede acceder por índice)

# frutas = {"Manzana", "Naranja", "Mandarina", "Naranja"}
# print(frutas)
# print(type(frutas))
# print(len(frutas))

# print("Manzana" in frutas)
# print("Pera" not in frutas)

# #add
# frutas.add("Pera")
# print(frutas)

# # Update
# frutasTropicales = {"Piña", "Mango"}
# frutas.update(frutasTropicales)
# print(frutas)

# # Eliminar elementos
# # Remove
# frutas.remove("Mango")
# print(frutas)

# # Discard
# frutas.discard("Mandarina")
# print(frutas)

# # Pop
# frutas.pop() # Elimina al azar
# print(frutas)

# # Clear
# frutas.clear()
# print(frutas)


# conjuntos = {"Python", 156, True}
# print(conjuntos)

# for item in conjuntos:
#     print(item)



print("------------------------------------------------")

a = {"a", "b", "c"}
b = {"c", "d", "e"}

# Union
c = a.union(b) 
print(c) # Tiene todos los elemtos pero c no se repite

# Interseccion
i = a.intersection(b)
print(i)

# Diferencia
d = a.difference(b)
print(d)