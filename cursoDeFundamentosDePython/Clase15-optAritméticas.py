x = 5
y = 10

# Suma +
print("5 + 10 es igual a:", x + y)  # Output: 15

# Resta -
print("5 - 10 es igual a:", x - y)  # Output: -5

# Multiplicación *
print("5 * 10 es igual a:", x * y)  # Output:   50

# División / (retorna un float)
print("10 / 5 es igual a:", y / x)  # Output: 2.0 ()

# División entera // (retorna un int)
print("10 // 4 es igual a:", y // 4)  # Output: 2 No decimal

# Módulo % (retorna el residuo de la división)
print("10 % 3 es igual a:", y % 3)  # Output: 1

# Exponenciación ** (eleva a la potencia)
print("5 elevado a la 3 es igual a:", x ** 3) # 5 * 5 * 5  Output: 125


#Saber si un número es par o impar usando el operador módulo
par = 8
print("8 es par?", par % 2 == 0) # Output: True
impar = 7
print("7 es impar?", impar % 2 == 0) # Output: False


"""
PRECEDENCIA DE OPERADORES

Paréntesis ()
Exponentiación **
Multiplicación *, División /, División entera //, Módulo %
Suma +, Resta -
Comparaciones de identidad y pertenencia
Lógicos not, and, or
"""