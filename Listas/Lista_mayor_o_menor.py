import random

numeros_aleatorios = []

for i in range(10):
    numero = random.randint(10, 20)
    numeros_aleatorios.append(numero)

mayor = numeros_aleatorios[0]
menor = numeros_aleatorios[0]

for numero in numeros_aleatorios:
    if numero > mayor:
        mayor = numero
    if numero < menor:
        menor = numero

print("Lista de números aleatorios:", numeros_aleatorios)
print("El número mayor es:", mayor)
print("El número menor es:", menor)
