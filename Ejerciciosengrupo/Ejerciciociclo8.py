n = int(input("Ingresa un número entero positivo: "))

multiplos = []
for i in range(1, n+1):
    if i % 5 == 0:
        multiplos.append(i)

if len(multiplos) == 0:
    print("No hay múltiplos de 5 entre 1 y", n)
else:
    print("Los múltiplos de 5 entre 1 y", n, "son:", multiplos)
    