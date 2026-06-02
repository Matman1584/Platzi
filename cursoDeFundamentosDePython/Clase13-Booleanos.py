v = True
f = False

print(v)  # Output: True
print(f)  # Output: False


print(type(v))  # Output: <class 'bool'>

print(bool("Hola Mundo"))  # Output: True
print(bool(""))  # Output: False


# TRUE
print(bool("abc"))  # Output: True
print(bool(123))  # Output: True
print(bool(["Manzana", "Pera"]))  # Output: True

# FALSE
print(bool(""))  # Output: False
print(bool(0))  # Output: False
print(bool([]))  # Output: False
print(bool(None))  # Output: False


# Saber si una variable corresponde a un entero
x = 123
print(isinstance(x, int))  # Output: True