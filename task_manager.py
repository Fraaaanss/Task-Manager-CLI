import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TASK_FILE = os.path.join(BASE_DIR, "tasks.txt")

tasks = []


# CARGAR TAREAS DESDE EL ARCHIVO
def load_tasks():

    # Verifica si el archivo existe
    if not os.path.exists(TASK_FILE):
        return

    # Abre el archivo en modo lectura
    with open(TASK_FILE, "r", encoding="utf-8") as file:

        # Lee línea por línea
        for line in file:

            # Elimina saltos de línea
            tarea = line.strip()

            # Verifica que no esté vacía
            if tarea and tarea != "****TAREAS****:":

                # Agrega la tarea a la lista
                tasks.append(tarea)


# GUARDAR TAREAS EN EL ARCHIVO
def save_tasks():

    # Abre el archivo en modo escritura
    with open(TASK_FILE, "w", encoding="utf-8") as file:

        # Título del archivo
        file.write("****TAREAS****:\n")

        # Escribe cada tarea
        file.write("\n".join(tasks))


# MENÚ
def menu():

    print("\n=== TASK MANAGER ===")
    print("1. Crear tarea")
    print("2. Listar tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Buscar tarea")
    print("6. Guardar tareas")
    print("7. Salir")


# CARGA LAS TAREAS AL INICIAR
load_tasks()


# CICLO PRINCIPAL
while True:

    # Muestra menú
    menu()

    # Pide opción
    option = input("Seleccione una opción: ")


    # CREAR TAREA
    if option == "1":

        tarea = input("Ingrese la descripción de la tarea: ")

        # Agrega la tarea
        tasks.append(tarea)

        # Guarda automáticamente
        save_tasks()

        print("Tarea agregada y guardada en tasks.txt.")


    # LISTAR TAREAS
    elif option == "2":

        # Verifica si hay tareas
        if len(tasks) == 0:

            print("No hay tareas registradas.")

        else:

            print("\n=== LISTA DE TAREAS ===")

            # Recorre las tareas
            for i, tarea in enumerate(tasks):

                print(f"{i + 1}. {tarea}")


    # COMPLETAR TAREA
    elif option == "3":

        if len(tasks) == 0:

            print("No hay tareas.")

        else:

            print("\n=== TAREAS ===")

            for i, tarea in enumerate(tasks):

                print(f"{i + 1}. {tarea}")

            # Pide número
            num = int(input("Número de tarea completada: "))

            # Marca como completada
            tasks[num - 1] = "✔ " + tasks[num - 1]

            # Guarda cambios
            save_tasks()

            print("Tarea completada.")


    # ELIMINAR TAREA
    elif option == "4":

        if len(tasks) == 0:

            print("No hay tareas.")

        else:

            print("\n=== TAREAS ===")

            for i, tarea in enumerate(tasks):

                print(f"{i + 1}. {tarea}")

            # Pide número
            num = int(input("Número de tarea a eliminar: "))

            # Elimina tarea
            tasks.pop(num - 1)

            # Guarda cambios
            save_tasks()

            print("Tarea eliminada.")


    # BUSCAR TAREA
    elif option == "5":

        buscar = input("Ingrese texto a buscar: ")

        encontrado = False

        # Recorre tareas
        for tarea in tasks:

            # Busca coincidencias
            if buscar.lower() in tarea.lower():

                print(tarea)

                encontrado = True

        if not encontrado:

            print("No se encontraron tareas.")


    # GUARDAR TAREAS
    elif option == "6":

        save_tasks()

        print("Tareas guardadas correctamente.")


    # SALIR
    elif option == "7":

        print("Saliendo...")
        break


    # OPCIÓN INVÁLIDA
    else:

        print("Opción inválida.")