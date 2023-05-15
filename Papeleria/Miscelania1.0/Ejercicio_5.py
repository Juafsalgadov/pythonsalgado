import random

def generar_arreglo(n):
    arreglo = []
    valor_anterior = random.randint(1, 10)
    arreglo.append(valor_anterior)

    for _ in range(n - 1):
        valor_siguiente = random.randint(valor_anterior + 1, (valor_anterior // 10 + 1) * 10)
        arreglo.append(valor_siguiente)
        valor_anterior = valor_siguiente

    return arreglo

n = int(input("Ingrese el número de elementos para el arreglo: "))
arreglo = generar_arreglo(n)

print("Arreglo generado:")
print(arreglo)