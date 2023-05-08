import random
n = int(input("Ingrese el número de elementos para la lista: "))
numeros = []
for i in range(n):
    numero = random.randint(1, 100)
    numeros.append(numero)
primer_numero = numeros[0]
print("El primer número de la lista es:", primer_numero)
suma = 0
for numero in numeros:
    suma += numero
print("La suma de los números es:", suma)
promedio = suma / n
print("El promedio de los números es:", promedio)
mayor = numeros[0]
for numero in numeros:
    if numero > mayor:
        mayor = numero
print("El número mayor de la lista es:", mayor)
menor = numeros[0]
for numero in numeros:
    if numero < menor:
        menor = numero
print("El número menor de la lista es:", menor)
i = 0
print("Lista generada: ", numeros)
while i < n-1:
    j = i + 1
    while j < n:
        if numeros[i] > numeros[j]:
            numeros[i], numeros[j] = numeros[j], numeros[i]
        j += 1
    i += 1
print("La lista ordenada en orden ascendente es:", numeros)
i = 0
while i < n-1:
    j = i + 1
    while j < n:
        if numeros[i] < numeros[j]:
            numeros[i], numeros[j] = numeros[j], numeros[i]
        j += 1
    i += 1
print("La lista ordenada en orden descendente es:", numeros)
frecuencias = {}
for numero in numeros:
    if numero in frecuencias:
        frecuencias[numero] += 1
    else:
        frecuencias[numero] = 1
moda = []
frecuencia_maxima = max(frecuencias.values())
for numero, frecuencia in frecuencias.items():
    if frecuencia == frecuencia_maxima:
        moda.append(numero)
print("La moda de la lista es:", moda)