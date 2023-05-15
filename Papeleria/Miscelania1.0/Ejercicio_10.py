def calcular_factorial(numero):
    factorial = 1
    for i in range(2, numero + 1):
        factorial *= i
    return factorial

def obtener_factoriales(lista):
    factoriales = []
    for num in lista:
        factorial = calcular_factorial(num)
        factoriales.append(factorial)
    return factoriales

numeros = list(range(2, 16))

factoriales = obtener_factoriales(numeros)

print("Números:", numeros)
print("Factoriales:", factoriales)
