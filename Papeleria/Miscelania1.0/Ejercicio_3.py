def generar_fibonacci(num_digitos):
    fibonacci = [0, 1] 
    while True:
        siguiente_num = fibonacci[-1] + fibonacci[-2]
        if len(str(siguiente_num)) > num_digitos:
            break
        fibonacci.append(siguiente_num)
    return fibonacci

num_digitos = int(input("Ingrese la cantidad de dígitos límite para la serie de Fibonacci: "))
serie_fibonacci = generar_fibonacci(num_digitos)

print("Serie de Fibonacci con", num_digitos, "dígitos:")
print(serie_fibonacci)