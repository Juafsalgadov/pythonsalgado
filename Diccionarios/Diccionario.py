def agregar_palabra(diccionario):
    palabra = input("Ingrese la palabra en español: ")
    traduccion = input("Ingrese la traducción en inglés: ")
    diccionario[palabra] = traduccion
    print("La palabra se ha agregado al diccionario.")


def traducir_palabra(diccionario):
    palabra = input("Ingrese la palabra que desea traducir: ")
    if palabra in diccionario:
        traduccion = diccionario[palabra]
        print(f"La traducción de '{palabra}' es '{traduccion}'.")
    else:
        print("La palabra no se encuentra en el diccionario.")


diccionario_espanol_ingles = {}
diccionario_ingles_espanol = {}

while True:
    print("------ Menú ------")
    print("1. Agregar palabra al diccionario español-inglés.")
    print("2. Agregar palabra al diccionario inglés-español.")
    print("3. Traducir palabra del español al inglés.")
    print("4. Traducir palabra del inglés al español.")
    print("5. Salir.")
    
    opcion = input("Ingrese una opción (1-5): ")
    
    if opcion == "1":
        agregar_palabra(diccionario_espanol_ingles)
    elif opcion == "2":
        agregar_palabra(diccionario_ingles_espanol)
    elif opcion == "3":
        traducir_palabra(diccionario_espanol_ingles)
    elif opcion == "4":
        traducir_palabra(diccionario_ingles_espanol)
    elif opcion == "5":
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida (1-5).")