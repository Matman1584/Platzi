# Función: es un bloque de código que solo se ejecuta cuando la llamamos. Permiten organizar y modularizar el código (reutilización)

def saludar(nombre, nacionalidad = "Colombia"): # Argumentos
    print("Hola", nombre, "de", nacionalidad)

# saludar("Pedro", "España") # Parámetros
# saludar("María") # Parámetro
# saludar("Ana")

def sumar(a,b): # Argumentos ya que son variables
    return a + b


resultado = sumar(2,3) # Parámentros por ser datos sueltos
print(resultado)

def funcion():
    pass

print("------------------------------------------")

def restar(c,d):
    return c - d

resultado_restar = restar(12,5)
print(resultado_restar)


print("----------------------------------------------")

def multiplicar(e,f):
    return e * f

resultado_multiplicar = multiplicar(12,4) # Output: 48
print(resultado_multiplicar)


print("--------------------------------------------")

def dividir(g,h):
    return g / h

resultado_dividir = dividir(30,5) # Output: 6.0
print(resultado_dividir)