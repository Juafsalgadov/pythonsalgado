import random

def generar_arreglo(n):
    arreglo = []
    for _ in range(n):
        arreglo.append(random.randint(1, 100))
    return arreglo

def sumar_pares(arreglo):
    suma = 0
    for num in arreglo:
        if num % 2 == 0:
            suma += num
    return suma

def promedio_impares(arreglo):
    impares = [num for num in arreglo if num % 2 != 0]
    if len(impares) == 0:
        return 0
    promedio = sum(impares) / len(impares)
    return promedio
n = int(input("Ingrese el número de elementos para el arreglo: "))
arreglo = generar_arreglo(n)

suma_pares = sumar_pares(arreglo)
promedio_impares = promedio_impares(arreglo)

print("Arreglo generado:", arreglo)
print("Suma de los números pares:", suma_pares)
print("Promedio de los números impares:", promedio_impares)
