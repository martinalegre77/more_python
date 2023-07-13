"""
RECURSIVIDAD
"""

def recursive(n):
    if n > 1:
        return n * recursive(n-1)
    elif n == 1 or n == 0:
        return 1

resultado = recursive(200)
print(resultado)


