import random

numeros_aleatorios = []

for i in range(1):
    numero = random.randint(10, 20)
    numeros_aleatorios.append(numero)

promedio = sum(numeros_aleatorios) / len(numeros_aleatorios)

print("Lista de números aleatorios:", numeros_aleatorios)
print("Promedio de los números aleatorios:", promedio)
