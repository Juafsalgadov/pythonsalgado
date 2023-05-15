import random

def generar_arreglo(n):
    arreglo = []
    for _ in range(n):
        arreglo.append(random.randint(1, 100))
    return arreglo

def ordenar_burbuja_ascendente(arreglo):
    n = len(arreglo)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arreglo[j] > arreglo[j + 1]:
                arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]
    return arreglo

def ordenar_burbuja_descendente(arreglo):
    n = len(arreglo)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arreglo[j] < arreglo[j + 1]:
                arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]
    return arreglo

n = int(input("Ingrese el número de elementos para el arreglo: "))
arreglo = generar_arreglo(n)

arreglo_ascendente = ordenar_burbuja_ascendente(arreglo[:])
arreglo_descendente = ordenar_burbuja_descendente(arreglo[:])

print("Arreglo generado:", arreglo)
print("Arreglo ordenado de menor a mayor:", arreglo_ascendente)
print("Arreglo ordenado de mayor a menor:", arreglo_descendente)
