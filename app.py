"""Gestor de tareas por consola."""

def mostrar_menu():
    """Muestra las opciones disponibles."""
    print("\n=== GESTOR DE TAREAS AVANZADO ===")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("0. Salir")


def completar_tarea():
    print("Función para completar tareas.")


def eliminar_tarea():
    print("Función para eliminar tareas.")


def main():
    mostrar_menu()
    completar_tarea()
    eliminar_tarea()


if __name__ == "__main__":
    main()
