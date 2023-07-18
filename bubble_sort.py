"""
Algoritmos de ordenamiento
BUBBLE SORT

Preguntar entre elemento 1 y 2
Cambiar si es mayor
Ciclar hasta que no haya cambios
"""

import random

lista = []

def mySort(list):
    print(f"La lista en proceso es: {list}")
    contador = False
    for i in range(0, len(list)):
        if i+1 == len(list):
            continue
        else:
            a, b = list[i], list[i+1]
            if list[i] > list[i+1]:
                contador = True
                list[i] = b
                list[i+1] = a
    if contador:
        mySort(list)
    else:
        print(f"La lista final es: {list}")
    
for i in range(10):
    lista.append(random.randint(1,30))

mySort(lista)

