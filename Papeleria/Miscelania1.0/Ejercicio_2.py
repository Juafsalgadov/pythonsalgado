import random

def generar_arreglo(n):
    arreglo = []
    for _ in range(n):
        arreglo.append(random.randint(1, 100))
    return arreglo

def comparar_arreglos(arreglo1, arreglo2):
    suma_arreglo1 = sum(arreglo1)
    suma_arreglo2 = sum(arreglo2)
    max_suma = max(suma_arreglo1, suma_arreglo2)

    max_arreglo1 = max(arreglo1)
    max_arreglo2 = max(arreglo2)
    max_numero = max(max_arreglo1, max_arreglo2)

    min_arreglo1 = min(arreglo1)
    min_arreglo2 = min(arreglo2)
    min_numero = min(min_arreglo1, min_arreglo2)

    promedio_conjunto = (sum(arreglo1) + sum(arreglo2)) / (len(arreglo1) + len(arreglo2))
    promedio_arreglo1 = sum(arreglo1) / len(arreglo1)
    promedio_arreglo2 = sum(arreglo2) / len(arreglo2)

    if promedio_arreglo1 > promedio_conjunto:
        promedio_arreglo1_estado = "por encima"
    else:
        promedio_arreglo1_estado = "por debajo"

    if promedio_arreglo2 > promedio_conjunto:
        promedio_arreglo2_estado = "por encima"
    else:
        promedio_arreglo2_estado = "por debajo"

    pares_arreglo1 = sum(1 for num in arreglo1 if num % 2 == 0)
    pares_arreglo2 = sum(1 for num in arreglo2 if num % 2 == 0)

    impares_arreglo1 = len(arreglo1) - pares_arreglo1
    impares_arreglo2 = len(arreglo2) - pares_arreglo2

    return (max_suma, max_numero, min_numero, promedio_conjunto,
            promedio_arreglo1, promedio_arreglo1_estado,
            promedio_arreglo2, promedio_arreglo2_estado,
            pares_arreglo1, pares_arreglo2,
            impares_arreglo1, impares_arreglo2)
n = int(input("Ingrese el número de elementos para cada arreglo: "))
arreglo1 = generar_arreglo(n)
arreglo2 = generar_arreglo(n)

resultado = comparar_arreglos(arreglo1, arreglo2)
print("Comparación de arreglos:")
print("Suma más alta:", resultado[0])
print("Número más alto:", resultado[1])
print("Número más bajo:", resultado[2])
print("Promedio conjunto:", resultado[3])
print("Promedio arreglo 1:", resultado[4], "(", resultado[5], "del promedio conjunto)")
print("Promedio arreglo 2:", resultado[6], "(", resultado[7], "del promedio conjunto)")
print("Cantidad de pares en arreglo 1:", resultado[8])
print("Cantidad de pares en arreglo 2:", resultado[9])
print("Cantidad de impares en arreglo 1:", resultado[10])
print("Cantidad de impares en arreglo 2:", resultado[11])
