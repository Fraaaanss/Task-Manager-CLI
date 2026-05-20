import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TASK_FILE = os.path.join(BASE_DIR, "tasks.txt")
tasks = []

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return

    with open(TASK_FILE, "r", encoding="utf-8") as file:
        for line in file:
            tarea = line.strip()
            if tarea:
                tasks.append(tarea)


def save_tasks():
    with open(TASK_FILE, "w", encoding="utf-8") as file:
        file.write("****TAREAS****:\n")
        file.write("\n".join(tasks))

def menu():
    print("\n=== TASK MANAGER ===")
    print("1. Crear tarea")
    print("2. Listar tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Buscar tarea")
    print("6. Guardar tareas")
    print("7. Salir")
    
load_tasks()

while True:
    menu()
    option = input("Seleccione una opción: ")
    if option == "1":
        tarea = input("Ingrese la descripción de la tarea: ")
        tasks.append(tarea)
        save_tasks()
        print("Tarea agregada y guardada en tasks.txt.")

    elif option == "2":
        if len(tasks) == 0:

            print("No hay tareas registradas.")

        else:

            print("\n=== LISTA DE TAREAS ===")

            for i, tarea in enumerate(tasks):

                print(f"{i + 1}. {tarea}")


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