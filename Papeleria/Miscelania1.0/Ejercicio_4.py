import random

def generar_arreglo_sin_repetir(n):
    arreglo = []
    numeros = set()

    while len(arreglo) < n:
        num = random.randint(1, 100)
        if num not in numeros:
            arreglo.append(num)
            numeros.add(num)
        else:
            print("El número", num, "ya está en el arreglo")

    return arreglo
n = int(input("Ingrese el número de elementos para el arreglo: "))
arreglo = generar_arreglo_sin_repetir(n)

print("Arreglo generado:")
print(arreglo)