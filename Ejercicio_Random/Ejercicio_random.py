import random
numero_aleatorio = random.randint(1, 100)
adivinanza = int(input("Adivina el número (entre 1 y 100): "))
while adivinanza != numero_aleatorio:
    if adivinanza < numero_aleatorio:
        print("El número es mayor")
    else:
        print("El número es menor")
    adivinanza = int(input("Adivina de nuevo: "))
print("¡Adivinaste el número!")