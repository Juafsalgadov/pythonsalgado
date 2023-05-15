import random

def generar_arreglo(n):
    arreglo = []
    for _ in range(n):
        arreglo.append(random.randint(1, 100))
    return arreglo

def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def identificar_primos(arreglo):
    primos = []
    for num in arreglo:
        if es_primo(num):
            primos.append(num)
    return primos

n = int(input("Ingrese el número de elementos para el arreglo: "))
arreglo = generar_arreglo(n)

primos = identificar_primos(arreglo)

print("Arreglo generado:", arreglo)
print("Números primos encontrados:", primos)
print("Cantidad de números primos:", len(primos))
