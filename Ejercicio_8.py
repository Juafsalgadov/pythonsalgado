Numero_mas_grande = -999999999
Numero = int(input("Introduce un número o escribe 1 para detener: "))
while Numero != 1:
    if Numero > Numero_mas_grande:
        Numero_mas_grande = Numero
    Numero = int(input("Introduce un número o escribe -1 para detener: "))
print("El número más grande es:", Numero_mas_grande)