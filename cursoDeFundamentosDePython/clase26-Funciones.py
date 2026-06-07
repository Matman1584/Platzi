# Función: es un bloque de código que solo se ejecuta cuando la llamamos. Permiten organizar y modularizar el código (reutilización)

def saludar(nombre, nacionalidad = "Colombia"): # Argumentos
    print("Hola", nombre, "de", nacionalidad)

saludar("Pedro", "España") # Parámetros
saludar("María") # Parámetro
saludar("Ana")
