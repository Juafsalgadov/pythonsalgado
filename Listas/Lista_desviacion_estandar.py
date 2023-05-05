numeros_ingresados = []
while True:
    numero = int(input("Ingrese un número entre 10 y 20 (0 para detenerse): "))
    if numero == 0:
        break
    elif numero < 10 or numero > 20:
        print("Número fuera del rango.")
    else:
        numeros_ingresados.append(numero)
suma_numeros = 0
for numero in numeros_ingresados:
    suma_numeros += numero
media = suma_numeros / len(numeros_ingresados)
diferencias_al_cuadrado = 0
for numero in numeros_ingresados:
    diferencia = numero - media
    diferencia_al_cuadrado = diferencia ** 2
    diferencias_al_cuadrado += diferencia_al_cuadrado
desviacion_estandar = (diferencias_al_cuadrado / len(numeros_ingresados)) ** 0.5
print(f"La desviación estándar de los números ingresados es: {desviacion_estandar}")
