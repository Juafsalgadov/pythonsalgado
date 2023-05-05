numeros = []
while True:
    num = int(input("Ingresa un número entre 10 y 20 (ingresa -1 para terminar): "))
    if num == -1:
        break
    elif num < 10 or num > 20:
        print("El número ingresado no está en el rango permitido.")
    else:
        numeros.append(num)
suma = 0
for num in numeros:
    suma += num
menor = numeros[0]
mayor = numeros[0]
for num in numeros:
    if num < menor:
        menor = num
    elif num > mayor:
        mayor = num
moda = None
max_frecuencia = 0
for num in numeros:
    frecuencia = numeros.count(num)
    if frecuencia > max_frecuencia:
        moda = num
        max_frecuencia = frecuencia
numeros_ordenados = sorted(numeros)
n = len(numeros_ordenados)
if n % 2 == 0:
    mediana = (numeros_ordenados[n//2 - 1] + numeros_ordenados[n//2]) / 2
else:
    mediana = numeros_ordenados[n//2]
n = len(numeros)
if n == 1:
    desviacion_estandar = 0
else:
    media = suma / n
    sumatoria = 0
    for num in numeros:
        sumatoria += (num - media) ** 2
    desviacion_estandar = (sumatoria / (n - 1)) ** 0.5
print("La lista de números ingresados es:", numeros)
print("La suma de los números ingresados es:", suma)
print("El número mayor ingresado es:", mayor)
print("El número menor ingresado es:", menor)
print("La moda de los números ingresados es:", moda)
print("La mediana de los números ingresados es:", mediana)
print("La desviación estándar de los números ingresados es:", desviacion_estandar)

