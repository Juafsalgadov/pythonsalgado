import random

def generar_arreglo(n):
    arreglo = []
    for _ in range(n):
        arreglo.append(random.randint(1, 100))
    return arreglo

def comparar_con_promedio(arreglo):
    promedio = sum(arreglo) / len(arreglo)
    resultados = []

    for num in arreglo:
        if num > promedio:
            resultados.append("por encima")
        elif num < promedio:
            resultados.append("por debajo")
        else:
            resultados.append("igual")

    return resultados

n = int(input("Ingrese el número de elementos para el arreglo: "))
arreglo = generar_arreglo(n)

resultado = comparar_con_promedio(arreglo)

print("Arreglo generado:", arreglo)
print("Comparación con el promedio:")
for i in range(n):
    print(arreglo[i], "-", resultado[i])