import random

numeros_aleatorios = []

for i in range(10):
    numero = random.randint(1, 20)
    numeros_aleatorios.append(numero)

resta = numeros_aleatorios[0]
for i in range(1, len(numeros_aleatorios)):
    resta -= numeros_aleatorios[i]

print("Lista de números aleatorios:", numeros_aleatorios)
print("Resta de los números aleatorios:", resta)
