x = 5
y = 3
z = 1

if x > y and x > z:
    print("x es mayor a y")
elif x == y:
    print("x es igual a y")
else:
    print("Ninguna de las condiciones anteriores se cumple") 


if x < y or  x > z:
    print("Que gane el trigre")



a = "Python"
b = " JavaScript"
c = "Python"

if a == b:
    print("a es igual a b")
else:
    print("a no es igual a b")



# IF ANIDADO
if a == c:
    if a != b:
        print("a es igual a c, pero es distinto a b")
    else:
        print("Estoy saliendo por el eslse del if aninado")
else:
    print("Topoyiyo rocks")



e = 10
f = 10

if e == f:
    pass # Para ignorar la estructura if hasta que definamos que comportamiento se espera