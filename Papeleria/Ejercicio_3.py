num = int(input("Ingrese la cantidad de dígitos Fibonacci: "))
a, b = 0, 1
fibonacci = []
while len(str(b)) <= num:
    fibonacci.append(b)
    a, b = b, a + b
print(fibonacci)
