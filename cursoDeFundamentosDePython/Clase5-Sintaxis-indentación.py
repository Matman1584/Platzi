"""
La sintaxis es el conjunto de reglas gramaticales que determinan cómo debe escribirse el código para que el intérprete lo entienda, mientras que la indentación es el uso de espacios al inicio de una línea para definir la jerarquía y los bloques de código.

Sintaxis en Python

Define la estructura formal del lenguaje. Si rompes una regla de sintaxis, Python genera un SyntaxError antes de ejecutar el programa.

 -- Es sensible a mayúsculas y minúsculas (if es válido, IF genera error).

 -- No requiere puntos y comas ; al final de las líneas.

 -- Los bloques lógicos (funciones, condicionales, bucles) se inician con dos puntos :.
"""

# Sintaxis correcta
mensaje = "Hola mundo"
if True:
    print(mensaje)

# Error de sintaxis (SyntaxError): falta cerrar la comilla
mensaje = "Hola mundo


"""
Indentación en Python

A diferencia de lenguajes como C, Java o JavaScript que usan llaves {} para agrupar código, Python utiliza la sangría (habitualmente 4 espacios por nivel). La indentación le indica a Python qué líneas pertenecen a una función, condicional o bucle específico.
"""
# Indentación correcta
edad = 20

if edad >= 18:
    print("Eres mayor de edad")  # Pertenece al bloque del 'if' (4 espacios)
    print("Acceso permitido")  # Pertenece al bloque del 'if' (4 espacios)

print("Programa finalizado")  # Fuera del 'if' (0 espacios, se ejecuta siempre)

"""
Si no respetas la sangría o mezclas espacios con tabuladores de forma inconsistente, obtendrás un IndentationError:
"""


# Error de indentación (IndentationError)
def saludar():
print("Hola")  # Fallo: la línea dentro de la función requiere 4 espacios de sangría


"""
# EL PROFESOR HIZO
- Creó un perfil para python en VScode
- Explicó la indentación y ya.
"""
