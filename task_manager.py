tasks = []

def menu():
    print("\n=== TASK MANAGER ===")
    print("1. Crear tarea")
    print("2. Listar tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Buscar tarea")
    print("6. Guardar tareas")
    print("7. Salir")

while True:
    menu()
    option = input("Seleccione una opción: ")

    if option == "1":
        tarea = input("Ingrese la descripción de la tarea: ")
        tasks.append(tarea)
        print("Tarea agregada.")

    elif option == "2":
        pass

    elif option == "3":
        pass

    elif option == "4":
        pass

    elif option == "5":
        pass

    elif option == "6":
        pass

    elif option == "7":
        print("Saliendo...")
        break