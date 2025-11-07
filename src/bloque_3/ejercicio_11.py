from rich.console import Console

console = Console()
ARCHIVO_TAREAS = "tareas.txt"

def agregar_tarea(tarea: str) -> None:
    """Agrega una tarea al final del archivo tareas.txt"""
    with open(ARCHIVO_TAREAS, "a", encoding="utf-8") as archivo:
        archivo.write(tarea + "\n")
    console.print(f"[green]Tarea agregada:[/green] {tarea}")

def ver_tareas() -> list[str]:
    """Lee todas las tareas del archivo y devuelve una lista"""
    try:
        with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as archivo:
            tareas = [linea.strip() for linea in archivo if linea.strip()]
        console.print("[blue]Lista de tareas:[/blue]")
        for i, tarea in enumerate(tareas, 1):
            console.print(f"{i}. {tarea}")
        return tareas
    except FileNotFoundError:
        console.print("[yellow]No hay tareas aún.[/yellow]")
        return []

def main() -> None:
    """Menú principal para gestionar tareas"""
    while True:
        console.print("\n[bold cyan]Gestor de Tareas[/bold cyan]")
        console.print("1. Ver tareas")
        console.print("2. Agregar tarea")
        console.print("3. Salir")
        opcion = console.input("Seleccione una opción (1-3): ").strip()

        if opcion == "1":
            ver_tareas()
        elif opcion == "2":
            tarea = console.input("Ingrese la tarea: ").strip()
            if tarea:
                agregar_tarea(tarea)
            else:
                console.print("[red]No se puede agregar tarea vacía[/red]")
        elif opcion == "3":
            console.print("[bold green]¡Hasta luego![/bold green]")
            break
        else:
            console.print("[red]Opción inválida, intente de nuevo[/red]")

if __name__ == "__main__":
    main()
