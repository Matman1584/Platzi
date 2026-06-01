print("Hola 'mundo'")  # Output: Hola 'mundo'
print('Hola "mundo"')  # Output: Hola "mundo"
print('''Hola 'mundo' "Python"''')  # Output: Hola 'mundo' "Python"
print("""Hola 'mundo' "Python" """)  # Output: Hola 'mundo' "Python"

#COMILLAS TRIPLES
saltoDeLinea = """Hola
mundo
desde
las
comillas
triples"""
print(saltoDeLinea)


#Metodo len
palabra = "Python"
print(len(palabra))


# Saber si una palabra está dentro de un texto
texto = "Este curso es de Fundamentos de Python"
estaIncluida = "Python" in texto
print(estaIncluida)  # Output: True

#saber si una palabra no está dentro de un texto
noEstaIncluida = "JavaScript" not in texto
print(noEstaIncluida)  # Output: True


# Convertir a mayúsculas
texto = "Este curso es de Fundamentos de Python"
mayuscula = texto.upper()
print(mayuscula) # Output: ESTE CURSO ES DE FUNDAMENTOS DE PYTHON


# Convertir a minúsculas
minuscula = texto.lower()
print(minuscula) # Output: este curso es de fundamentos de python


# Elimanr espacios en blanco al inicio y al final
textoConEspacios = "      Este es el texto         "
textosinEspacios = textoConEspacios.strip()
print(textosinEspacios) # Output: Este es el texto