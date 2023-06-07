from Clases import*
empleado1 = (Empleado.contador,"Juan Edilberto", "Administrador", 1160000)
print("Salario por hora:", empleado1.Salarioxhora())
print("Incremento con Ipc:", empleado1.Sumaipc())
print("Salario con 2 horas extras:", empleado1.horasextra(2))
print("Suma de los salarios:", Empleado.sumasalarios())
print("Promedio de los salarios:", Empleado.promediosalarios())