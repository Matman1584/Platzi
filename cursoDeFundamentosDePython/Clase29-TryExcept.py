try:
    numero = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir por 0")

try:
    print(x)
except NameError:
    print("Esta variable no ha sido definida")
finally:
    print("Esto será ejecutado siendo el bloque exitoso o no")