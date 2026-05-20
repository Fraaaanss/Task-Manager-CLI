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
#layla
while True:
    menu()
    option = input("Seleccione una opción: ")
    if option == "1":
        tarea = input("Ingrese la descripción de la tarea: ")
        tasks.append(tarea)
        save_tasks()
        print("Tarea agregada y guardada en tasks.txt.")
    #PAULA
    elif option == "2":
        pass
    #MILENA
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
    #NAIMA
    elif option == "4":
        pass
    #LUCETY
    elif option == "5":
        pass
    #FRANS
    elif option == "6":
        pass

    elif option == "7":
        print("Saliendo...")
        break