# Lambda es una función pequeña y anónima que puede tener muchos argumentos pero sólo una expresión

# Sintaxis lambda argumentos : expresión

# x = lambda a,b : a + b

# print(x(2,3)) # Output: 5

def mifuncion(n):
    return lambda a : a * n

duplicador = mifuncion(2) # Generadores
triplicador = mifuncion(3) # Generador
quintuplicador = mifuncion(5) # Generador

print(duplicador(5)) # Output: 10
print(triplicador(5)) # Output: 15
print(quintuplicador(5)) # Output: 25