import random
num = int(input("Ingrese el número de elementos para la lista: "))
numeros = []
while len(numeros) < num:
    nuevo_numero = random.randint(1, num*2)
    if nuevo_numero in numeros:
        print(f"El número {nuevo_numero} ya está en la lista.")
    else:
        numeros.append(nuevo_numero)
print(numeros)
