# ind 01234

texto = "Este es el texto"
"""
print(texto[0])  # Output: E
print(texto[4])  # Output: e
print(texto[6])  # Output: t
"""

# Slicing
"""
print(texto[0:4])  # Output: Este
print(texto[:7])  # Output: Este es
print(texto[8:14])  # Output: el texto
"""


# Slicing negativo
"""
print(texto[5:-2]) # resta o y t, Output: es el tex
"""


# Reemplazar una palábra de un texto
"""
curso = "Este curso es de JavaScript"
print(curso.replace("JavaScript", "Python"))  # Output: Este curso es de Python
"""


# Dividir texto cada que se encuentre un espacio
"""
texto2 = "Ayer comí calambre y hoy comeré alambre"
print(texto2.split(" ")) # Output: ['Ayer', 'comí', '
"""


# Buscar palabras en mayúsculas
texto3 = "Este testo tiene MAYUSCULAS y necesito econtrar ciertas palabras"
print("mayusculas".lower() in texto3.lower()) # Output: True