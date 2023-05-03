num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
if num1 > num2:
    mayor = num1
    menor = num2
else:
    mayor = num2
    menor = num1
cociente = 0
residuo = mayor

while residuo >= menor:
    residuo -= menor
    cociente += 1
print("El cociente de", mayor, "entre", menor, "es:", cociente)
print("El residuo de", mayor, "entre", menor, "es:", residuo)
