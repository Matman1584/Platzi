# Coleccion de pares clave valor (Ordenado a partir de Python 3.7)

auto = {
    "marca": "Renault",
    "modelo": "Clio",
    "año": 2025
}

# print(auto)
# print(auto["marca"])
# print(auto.keys())
# print(auto.values())

# if "marca" in auto:
#     print("Ostia que buen auto tío")

auto["año"] = 2026
print(auto)

auto["Color"] = "Verde"
print(auto)

auto.update({"año": 2022, "puertas": 4})
print(auto)

# auto.pop("puertas")
# print(auto)

# auto.popitem()
# print(auto)

# auto.clear()
# print(auto)

# for k in auto: # keys
#     print(k)

# for v in auto.values():
#     print(v)

print("---------------------------------------------")

# for k,v in auto.items(): # keys, value
#     print(k,v)


    # Diccionarios anidados
familia = {
    "hijo1" : {
        "nombre": "Pedro",
        "edad": 8
    },
    "hijo2" : {
        "nombre": "Ana",
        "edad": 7
    },
    "hijo3" : {
        "nombre": "Marcelo",
        "edad": 6
    },
}

print(familia["hijo1"]["nombre"])