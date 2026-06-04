"""
palabra = "Python"

for letra in palabra:
    print(letra)
"""

"""
frutas = ["Manzana", "Naranja", "Kiwi"] #Aqui creamos una lista

for fruta in frutas:
    if fruta == "Naranja":
        break # Si la fruta es igual a Naranja detente
    print(fruta)
"""


"""
frutas = ["Manzana", "Naranja", "Kiwi"] #Aqui creamos una lista
for frutiño in frutas:
    if frutiño == "Naranja":
        continue # Si frutiño igual Naranja la ignora
    print(frutiño)
else:
    print("Ya hemos terminado con el bucle for")
"""


"""
for i in range(10): #Empieza en y termina en 9
    print(i)
"""


"""
for i in range(12,15): # Se imprime de 12 a 14
    print(i)
"""


"""
for i in range(0,10,2):
    print(i)
"""

frutas = ["manzana", "naranja", "kiwi"]
adjetivos = ["Rica", "Saludable"]

for fruta in frutas:
    for adjetivo in adjetivos:
        print(adjetivo, fruta)


print("------------------------------------------")

    #TAREA Imprimir eseto en consola
"""
Manzana rica
Manzana saludable
Naranja rica
Naranja saludable
Kiwi rica
kiwi saludable
"""
for fruta in frutas:
    for adjetivo in adjetivos:
        print(fruta, adjetivo)
    