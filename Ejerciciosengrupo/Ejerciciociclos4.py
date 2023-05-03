def es_numero_perfecto(numero):
    suma_divisores = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma_divisores += i
    return suma_divisores == numero

def encontrar_numeros_perfectos():
    numeros_perfectos = []
    for i in range(1, 1001):
        if es_numero_perfecto(i):
            numeros_perfectos.append(i)
    return numeros_perfectos

numeros_perfectos = encontrar_numeros_perfectos()
cantidad_numeros_perfectos = len(numeros_perfectos)

print(f"Entre 1 y 1000 hay {cantidad_numeros_perfectos} números perfectos:")
print(numeros_perfectos)
