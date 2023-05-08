numeros_ingresados = []
while True:
    numero = int(input("Ingrese un número entre 10 y 20 (0 para detenerse): "))
    if numero == 0:
        break
    elif numero < 10 or numero > 20:
        print("Número fuera del rango.")
    else:
        numeros_ingresados.append(numero)
ocurrencias = {}
for numero in numeros_ingresados:
    if numero in ocurrencias:
        ocurrencias[numero] += 1
    else:
        ocurrencias[numero] = 1
moda = None
max_ocurrencias = 0
for numero, ocurrencia in ocurrencias.items():
    if ocurrencia > max_ocurrencias:
        moda = numero
        max_ocurrencias = ocurrencia
if moda is None:
    print("No hay moda")
elif max_ocurrencias > 1:
    print(f"La moda es: {moda}")
else:
    print("Todos los números ingresados son únicos")
