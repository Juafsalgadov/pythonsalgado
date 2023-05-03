num_lines = int(input("Ingrese el número de líneas que desea imprimir: "))

for i in range(num_lines):
    line = ""
    for j in range(i+1):
        line += "* "
    print(line)
