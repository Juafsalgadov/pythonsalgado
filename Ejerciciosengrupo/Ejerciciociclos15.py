n = int(input("Ingresa un valor no negativo: "))

for i in range(n, 0, -1):
    for j in range(1, i+1):
        print(j, end=' ')
    print()
