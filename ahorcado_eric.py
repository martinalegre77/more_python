"""
JUEGO DEL AHORCADO

1.- Ingresar palabra (a descubrir)
2.- 7 intentos
3.- Se ingresa letra por letra (hasta adivinar o terminar letras)
4.- Profit
"""
vida = 7
ganaste = False

palabra = input("Ingresá la palabra del ahorcado: ").lower()
secreta = " ".join(["_" for letra in palabra])
letras = []

print(secreta)

while True:
    letra = input("Decime una letra: ").lower()

    if letra in palabra:
        letras.append(letra)

        secreta = " ".join([letra if letra in letras else "_" for letra in palabra])
        print(secreta)

        if len(letras) == len(palabra):
            print("GANASTE!!!")
            break
    else:
        vida -= 1
        print(f"{letra} no está en la palabra")
        print(f"Te quedan {vida} vidas")
        if vida <= 0:
            print("PERDISTE!!!")
            break

