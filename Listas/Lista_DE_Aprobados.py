import random
calificaciones = [round(random.uniform(0, 5), 1) for _ in range(20)]
print("Calificaciones:", calificaciones)
aprobados = [calificacion for calificacion in calificaciones if calificacion >= 3]
reprobados = [calificacion for calificacion in calificaciones if calificacion < 3]
print("Aprobados:", aprobados)
print("Reprobados:", reprobados)
num_unidades = 5
calif_por_unidad = [[] for _ in range(num_unidades)]
aprobados_por_unidad = [[] for _ in range(num_unidades)]
reprobados_por_unidad = [[] for _ in range(num_unidades)]
for i, calificacion in enumerate(calificaciones):
    unidad = i // (len(calificaciones) // num_unidades)
    calif_por_unidad[unidad].append(calificacion)
    if calificacion >= 3:
        aprobados_por_unidad[unidad].append(calificacion)
    else:
        reprobados_por_unidad[unidad].append(calificacion)
for i, unidad in enumerate(calif_por_unidad):
    promedio_aprobados = sum(aprobados_por_unidad[i]) / len(aprobados_por_unidad[i]) if aprobados_por_unidad[i] else 0
    promedio_reprobados = sum(reprobados_por_unidad[i]) / len(reprobados_por_unidad[i]) if reprobados_por_unidad[i] else 0
    print(f"Unidad {i+1}: Calificaciones = {unidad}, Promedio de aprobados = {promedio_aprobados}, Promedio de reprobados = {promedio_reprobados}")