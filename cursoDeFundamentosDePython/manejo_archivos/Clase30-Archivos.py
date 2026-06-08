# open(nombre, modo)

# R (read) Lectura
# W (write) Escritura
# X (Crea archivo nuevo)

try:
    with open("archivo.txt", "r", encoding="utf-8") as f: # Leemos el archivo
        print(f.readline())
        print(f.readline())
except FileNotFoundError:
    open("archivo.txt", "x")
    print("No se ha encontrado el archivo")

# try:
#     with open("archivo.txt", "w") as f:   # Escribimos en el archivo 
#         f.write("Hola mundo desde write en el archivo principal")
#     with open("archivo.txt", "r", encoding="utf-8") as f:
#         print(f.readline())
# except FileNotFoundError:
#     print("No se ha encontrado el archivo")

try:
    with open("archivo.txt", "a") as append:   # Agregamos mensaje sin borrar lo que ya estaba escrito
        append.write("Primera linea")
        append.write("\nMensaje agregado usando append (no borra, agrega)") # append es solo una variable
    with open("archivo.txt", "r", encoding="utf-8") as append:
        print(append.readline())
except FileNotFoundError:
    print("No se ha encontrado el archivo")
