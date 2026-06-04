i = 1
'''
while i <= 10:
    print(i)
    i += 1 
'''

"""
Cada que se ejecute el bucle, suma 1 a i. Esto hace que
eventualmente i no sea menor a 10 y se deje de ejecutar
el bucle.
"""


'''
z = 0
while z <= 10:
    if z == 5: #Llega a 10 porque z nunca es iguala 5
        break
    z += 2
    print(z) 
'''


k = 0
while k < 10:
    k += 1 
    if k == 5:
        continue
    print(k)
else:
    print("k dejó de ser menor a 10")