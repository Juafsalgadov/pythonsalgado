import random
def generar_arreglo(n):
    arreglo = []
    for _ in range(n):
        arreglo.append(random.randint(1, 100))
    return arreglo
def imprimir_arreglo(arreglo):
    print("Arreglo original:")
    print(arreglo)
def suma(arreglo):
    return sum(arreglo)
def promedio(arreglo):
    return sum(arreglo) / len(arreglo)
def mayor(arreglo):
    return max(arreglo)
def menor(arreglo):
    return min(arreglo)
def ordenar_ascendente(arreglo):
    return sorted(arreglo)
def ordenar_descendente(arreglo):
    return sorted(arreglo, reverse=True)
def moda(arreglo):
    contador = {}
    for num in arreglo:
        if num in contador:
            contador[num] += 1
        else:
            contador[num] = 1
    max_frecuencia = max(contador.values())
    moda = [num for num, frecuencia in contador.items() if frecuencia == max_frecuencia]
    return moda
def mediana(arreglo):
    sorted_arreglo = sorted(arreglo)
    n = len(sorted_arreglo)
    if n % 2 == 0:
        return (sorted_arreglo[n//2 - 1] + sorted_arreglo[n//2]) / 2
    else:
        return sorted_arreglo[n//2]
def buscar_numero(arreglo, numero):
    posiciones = []
    contador = 0
    for i, num in enumerate(arreglo):
        if num == numero:
            posiciones.append(i)
            contador += 1
    if contador > 0:
        return f"El número {numero} se encuentra en las posiciones: {posiciones}. Aparece {contador} veces."
    else:
        return f"El número {numero} no se encuentra en el arreglo."
n = int(input("Ingrese el número de elementos para el arreglo: "))
arreglo = generar_arreglo(n)
while True:
    print("\nMENU:")
    print("a. Imprimir arreglo original")
    print("b. Suma")
    print("c. Promedio")
    print("d. Mayor")
    print("e. Menor")
    print("f. Ordenar ascendente")
    print("g. Ordenar descendente")
    print("h. Moda")
    print("i. Mediana")
    print("j. Buscar número")
    print("k. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "a":
        imprimir_arreglo(arreglo)
    elif opcion == "b":
        print("Suma:", suma(arreglo))
    elif opcion == "c":
        print("Promedio:", promedio(arreglo))
    elif opcion == "d":
        print("Mayor:", mayor(arreglo))
    elif opcion == "e":
        print("Menor:", menor(arreglo))
    elif opcion == "f":
        print("Arreglo ordenado ascendente:", ordenar_ascendente(arreglo))
    elif opcion == "g":
        print("Arreglo ordenado descendente:", ordenar_descendente(arreglo))
    elif opcion == "h":
        print("Moda:", moda(arreglo))
    elif opcion == "i":
        print("Mediana:", mediana(arreglo))
    elif opcion == "j":
        numero = int(input("Ingrese el número a buscar: "))
        print(buscar_numero(arreglo, numero))
    elif opcion == "k":
        break
    else:
        print("Opción inválida")