import random

numeros_aleatorios = []

for i in range(10):
    numero = random.randint(10, 20)
    numeros_aleatorios.append(numero)

suma = sum(numeros_aleatorios)

print("Lista de números aleatorios:", numeros_aleatorios)
print("Suma de los números aleatorios:", suma)
