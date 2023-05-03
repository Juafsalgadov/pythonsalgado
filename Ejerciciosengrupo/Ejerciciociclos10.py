def euclidean_algorithm(m, n):
    while n != 0:
        r = m % n
        m = n
        n = r
    return m

m = int(input("Ingrese el valor de m: "))
n = int(input("Ingrese el valor de n: "))

gcd = euclidean_algorithm(m, n)

print("El m.c.d de", m, "y", n, "es", gcd)
