from rich.console import Console
from rich.table import Table
import os

RUTA_ARCHIVO = "tareas.txt"
console = Console()


def agregar_tarea(tarea: str) -> None:
    """
    Agrega una tarea al archivo tareas.txt.
    Si el archivo no existe, lo crea automáticamente.
    """
    with open(RUTA_ARCHIVO, "a", encoding="utf-8") as archivo:
        archivo.write(tarea.strip() + "\n")


def ver_tareas() -> list[str]:
    """
    Lee todas las tareas del archivo y las devuelve como una lista.
    Si no hay tareas o el archivo no existe, devuelve una lista vacía.
    """
    if not os.path.exists(RUTA_ARCHIVO):
        return []

    with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
        tareas = [linea.strip() for linea in archivo.readlines() if linea.strip()]
    return tareas


def mostrar_tareas(tareas: list[str]) -> None:
    """
    Muestra las tareas en una tabla utilizando la librería rich.
    """
    if not tareas:
        console.print("[yellow]No hay tareas registradas.[/yellow]")
        return

    tabla = Table(title="📋 Lista de Tareas", show_lines=True)
    tabla.add_column("N°", justify="center", style="cyan")
    tabla.add_column("Tarea", style="green")

    for i, tarea in enumerate(tareas, start=1):
        tabla.add_row(str(i), tarea)

    console.print(tabla)


def menu_tareas():
    """
    Muestra el menú interactivo del gestor de tareas.
    """
    while True:
        console.print("\n[bold blue]--- Gestor de Tareas ---[/bold blue]")
        console.print("1. Agregar tarea")
        console.print("2. Ver tareas")
        console.print("3. Salir al menú principal")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            tarea = input("Ingrese la nueva tarea: ").strip()
            if tarea:
                agregar_tarea(tarea)
                console.print("[green]Tarea agregada correctamente.[/green]")
            else:
                console.print("[red]Debe ingresar una tarea válida.[/red]")

        elif opcion == "2":
            tareas = ver_tareas()
            mostrar_tareas(tareas)

        elif opcion == "3":
            console.print("[blue]Regresando al menú principal...[/blue]")
            break

        else:
            console.print("[red]Opción inválida. Intente de nuevo.[/red]")


if __name__ == "__main__":
    menu_tareas()
