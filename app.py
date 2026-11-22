"""Gestor de tareas por consola."""

tareas = []

def mostrar_menu():
    """Muestra las opciones disponibles."""
    print("\n=== GESTOR DE TAREAS ===")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("0. Salir")


def agregar_tarea():
    titulo = input("Escriba la tarea: ")
    tareas.append({"titulo": titulo, "completada": False})
    print("Tarea agregada correctamente.")


def listar_tareas():
    if not tareas:
        print("No hay tareas registradas.")
        return
    for indice, tarea in enumerate(tareas, start=1):
        estado = "Completada" if tarea["completada"] else "Pendiente"
        print(f"{indice}. {tarea['titulo']} - {estado}")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            listar_tareas()
        elif opcion == "0":
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
