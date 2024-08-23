
lista_estudiantes = []

def mostrar_menu():
    print("\nSistema de Gestión de Estudiantes")
    print("1. Añadir nuevo estudiante")
    print("2. Ver lista de estudiantes")
    print("3. Modificar datos de un estudiante")
    print("4. Borrar un estudiante")
    print("5. Salir del sistema")
    eleccion = input("Selecciona una opción (1/2/3/4/5): ")
    return eleccion

def añadir_estudiante():
    nombre_estudiante = input("Introduce el nombre del estudiante: ")
    edad_estudiante = int(input("Introduce la edad del estudiante: "))
    registro = {'nombre': nombre_estudiante, 'edad': edad_estudiante}
    lista_estudiantes.append(registro)
    print(f"{nombre_estudiante} ha sido añadido a la lista.")

def ver_estudiantes():
    if not lista_estudiantes:
        print("La lista de estudiantes está vacía.")
    else:
        print("Estudiantes registrados:")
        for idx, registro in enumerate(lista_estudiantes, start=1):
            print(f"{idx}. Nombre: {registro['nombre']}, Edad: {registro['edad']}")

def modificar_estudiante():
    ver_estudiantes()
    while True:
        try:
            seleccion = int(input("Selecciona el número del estudiante que deseas modificar: ")) - 1
            if 0 <= seleccion < len(lista_estudiantes):
                break
            else:
                print("Número fuera de rango. Intenta de nuevo.")
        except ValueError:
            print("Entrada inválida. Introduce un número.")

    registro = lista_estudiantes[seleccion]
    print(f"Estudiante seleccionado: {registro['nombre']} - {registro['edad']} años")
    
    nuevo_nombre = input("Nuevo nombre (o pulsa Enter para mantener el actual): ")
    nueva_edad = input("Nueva edad (o pulsa Enter para mantener la actual): ")

    if nuevo_nombre:
        registro['nombre'] = nuevo_nombre
    if nueva_edad:
        try:
            registro['edad'] = int(nueva_edad)
        except ValueError:
            print("Edad inválida. No se ha cambiado.")

    print(f"Información de {registro['nombre']} actualizada correctamente.")

def borrar_estudiante():
    ver_estudiantes()
    while True:
        try:
            seleccion = int(input("Selecciona el número del estudiante que deseas borrar: ")) - 1
            if 0 <= seleccion < len(lista_estudiantes):
                break
            else:
                print("Número fuera de rango. Intenta de nuevo.")
        except ValueError:
            print("Entrada inválida. Introduce un número.")

    registro = lista_estudiantes.pop(seleccion)
    print(f"El estudiante {registro['nombre']} ha sido eliminado de la lista.")

def iniciar_programa():
    while True:
        eleccion = mostrar_menu()
        if eleccion == '1':
            añadir_estudiante()
        elif eleccion == '2':
            ver_estudiantes()
        elif eleccion == '3':
            modificar_estudiante()
        elif eleccion == '4':
            borrar_estudiante()
        elif eleccion == '5':
            print("Cerrando el sistema...")
            break
        else:
            print("Opción incorrecta. Por favor, elige nuevamente.")

iniciar_programa()
