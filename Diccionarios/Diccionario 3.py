def agregar_animal(diccionario_espanol, diccionario_ingles):
    animal_espanol = input("Ingrese el nombre del animal en español: ")
    animal_ingles = input("Ingrese el nombre del animal en inglés: ")
    tupla_espanol = diccionario_espanol.get('animales', ())
    tupla_ingles = diccionario_ingles.get('animals', ())
    tupla_espanol += (animal_espanol,)
    tupla_ingles += (animal_ingles,)
    diccionario_espanol['animales'] = tupla_espanol
    diccionario_ingles['animals'] = tupla_ingles
    print("El animal se ha agregado a los diccionarios.")


diccionario_espanol = {'animales': ()}
diccionario_ingles = {'animals': ()}

while True:
    print("------ Menú ------")
    print("1. Agregar animal al diccionario español.")
    print("2. Agregar animal al diccionario inglés.")
    print("3. Salir.")

    opcion = input("Ingrese una opción (1-3): ")

    if opcion == "1":
        agregar_animal(diccionario_espanol, diccionario_ingles)
    elif opcion == "2":
        agregar_animal(diccionario_ingles, diccionario_espanol)
    elif opcion == "3":
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida (1-3).")