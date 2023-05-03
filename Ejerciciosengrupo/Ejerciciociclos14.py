for num in range(100, 1000):
    suma_cubos = 0
    for cifra in str(num):
        suma_cubos += int(cifra) ** 3
    if suma_cubos == num:
        print(num)
