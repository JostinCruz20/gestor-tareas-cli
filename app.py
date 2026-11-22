"""Gestor de tareas por consola."""

tareas = []

def mostrar_menu():
    """Muestra las opciones disponibles."""
    print("\n=== GESTOR DE TAREAS CLI v1.0 ===")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("0. Salir del programa")


def agregar_tarea():
    titulo = input("Escriba la tarea: ").strip()
    if not titulo:
        print("Error: el título de la tarea no puede estar vacío.")
        return
    tareas.append({"titulo": titulo, "completada": False})
    print("Tarea agregada correctamente.")


def listar_tareas():
    if not tareas:
        print("No hay tareas registradas.")
        return
    for indice, tarea in enumerate(tareas, start=1):
        estado = "Completada" if tarea["completada"] else "Pendiente"
        print(f"{indice}. {tarea['titulo']} - {estado}")


def completar_tarea():
    listar_tareas()
    try:
        numero = int(input("Número de la tarea a completar: "))
        tareas[numero - 1]["completada"] = True
        print("Tarea completada.")
    except (ValueError, IndexError):
        print("Número de tarea no válido.")


def eliminar_tarea():
    listar_tareas()
    try:
        numero = int(input("Número de la tarea a eliminar: "))
        tareas.pop(numero - 1)
        print("Tarea eliminada.")
    except (ValueError, IndexError):
        print("Número de tarea no válido.")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            listar_tareas()
        elif opcion == "3":
            completar_tarea()
        elif opcion == "4":
            eliminar_tarea()
        elif opcion == "0":
            print("Hasta luego.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
