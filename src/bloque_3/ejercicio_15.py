import json
import os
from typing import List, Dict, Union
from rich.console import Console
from rich.table import Table

# --- Configuración y Datos ---

BIBLIOTECA_FILE = "biblioteca.json"
console = Console()

Libro = Dict[str, Union[str, None]]


def inicializar_biblioteca() -> List[Libro]:
    """
    Carga los datos de la biblioteca desde el archivo JSON o crea un archivo de ejemplo.

    Returns:
        List[Libro]: Lista de diccionarios representando los libros.
    """
    if os.path.exists(BIBLIOTECA_FILE):
        try:
            with open(BIBLIOTECA_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            console.print("[bold red]Error:[/bold red] El archivo JSON está corrupto. Usando datos de ejemplo.")
            return _crear_datos_ejemplo()
    else:
        return _crear_datos_ejemplo()


def _crear_datos_ejemplo() -> List[Libro]:
    """Crea y guarda un conjunto de datos de libros de ejemplo."""
    libros = [
        {"libro_id": "001", "titulo": "Cien Años de Soledad", "autor": "García Márquez", "prestado_a": None},
        {"libro_id": "002", "titulo": "1984", "autor": "George Orwell", "prestado_a": "Juan Pérez"},
        {"libro_id": "003", "titulo": "El Señor de los Anillos", "autor": "J.R.R. Tolkien", "prestado_a": None},
        {"libro_id": "004", "titulo": "Don Quijote de la Mancha", "autor": "Cervantes", "prestado_a": "Ana Díaz"},
        {"libro_id": "005", "titulo": "Rayuela", "autor": "Julio Cortázar", "prestado_a": None},
    ]
    guardar_estado(libros)
    console.print(f"[bold yellow]Advertencia:[/bold yellow] Archivo '{BIBLIOTECA_FILE}' creado con datos de ejemplo.")
    return libros


def guardar_estado(libros: List[Libro]):
    """Guarda el estado actual de la biblioteca en el archivo JSON."""
    try:
        with open(BIBLIOTECA_FILE, 'w', encoding='utf-8') as f:
            json.dump(libros, f, indent=4, ensure_ascii=False)
    except IOError:
        console.print("[bold red]Error:[/bold red] No se pudo guardar el estado de la biblioteca.")


# --- Funciones Principales de Lógica ---

def prestar_libro(libros: List[Libro], libro_id: str, nombre_aprendiz: str) -> bool:
    """Marca un libro como prestado si está disponible."""
    for libro in libros:
        if libro['libro_id'] == libro_id:
            if libro['prestado_a'] is None:
                libro['prestado_a'] = nombre_aprendiz
                guardar_estado(libros)
                console.print(
                    f"[bold green]Éxito:[/bold green] '{libro['titulo']}' prestado a [yellow]{nombre_aprendiz}[/yellow].")
                return True
            else:
                console.print(
                    f"[bold red]Error:[/bold red] El libro ya está prestado a [yellow]{libro['prestado_a']}[/yellow].")
                return False
    console.print(f"[bold red]Error:[/bold red] Libro con ID '{libro_id}' no encontrado.")
    return False


def devolver_libro(libros: List[Libro], libro_id: str) -> bool:
    """Marca un libro como disponible."""
    for libro in libros:
        if libro['libro_id'] == libro_id:
            if libro['prestado_a'] is not None:
                prestado_a = libro['prestado_a']
                libro['prestado_a'] = None
                guardar_estado(libros)
                console.print(
                    f"[bold green]Éxito:[/bold green] '{libro['titulo']}' devuelto por [yellow]{prestado_a}[/yellow].")
                return True
            else:
                console.print(
                    f"[bold yellow]Advertencia:[/bold yellow] El libro '{libro['titulo']}' ya estaba disponible.")
                return False
    console.print(f"[bold red]Error:[/bold red] Libro con ID '{libro_id}' no encontrado.")
    return False


def buscar_libro(libros: List[Libro], query: str) -> List[Libro]:
    """Busca libros por título (insensible a mayúsculas)."""
    query = query.lower()
    resultados = [
        libro for libro in libros
        if query in libro.get('titulo', '').lower()
    ]
    return resultados


def ver_libros_prestados(libros: List[Libro]) -> List[Libro]:
    """Muestra todos los libros que están prestados."""
    prestados = [libro for libro in libros if libro['prestado_a'] is not None]
    return prestados


# --- Funciones de Presentación con Rich ---

def mostrar_tabla_libros(libros: List[Libro], titulo_tabla: str):
    """Muestra una lista de libros en una tabla atractiva usando Rich."""
    if not libros:
        console.print(f"\n[bold magenta]-- {titulo_tabla} --[/bold magenta]")
        console.print("[red]No se encontraron libros que coincidan con la búsqueda.[/red]\n")
        return

    table = Table(title=f"\n[bold cyan]{titulo_tabla}[/bold cyan]", show_header=True, header_style="bold blue")

    table.add_column("ID", style="dim", width=4)
    table.add_column("Título", style="bold white", min_width=30)
    table.add_column("Autor", style="yellow")
    table.add_column("Estado", style="white")

    for libro in libros:
        estado_style = "[bold red]Prestado[/bold red]" if libro['prestado_a'] else "[bold green]Disponible[/bold green]"
        estado_detalle = f"{estado_style} ([dim]{libro['prestado_a']}[/dim])" if libro['prestado_a'] else estado_style

        table.add_row(
            libro.get('libro_id', 'N/A'),
            libro.get('titulo', 'Título Desconocido'),
            libro.get('autor', 'Desconocido'),
            estado_detalle
        )

    console.print(table)
    print("\n")


def mostrar_menu():
    """Muestra el menú de opciones."""
    console.print("\n[bold]========== SISTEMA DE BIBLIOTECA ==========[/bold]", style="magenta")
    console.print("[bold yellow]1.[/bold yellow] Prestar Libro")
    console.print("[bold yellow]2.[/bold yellow] Devolver Libro")
    console.print("[bold yellow]3.[/bold yellow] Buscar Libro por Título")
    console.print("[bold yellow]4.[/bold yellow] Ver Libros Prestados")
    console.print("[bold yellow]5.[/bold yellow] Ver TODOS los Libros")
    console.print("[bold yellow]6.[/bold yellow] Salir", style="bold red")
    console.print("=============================================", style="magenta")


# --- Función Principal ---

def main():
    """Bucle principal de la aplicación de consola."""
    libros = inicializar_biblioteca()

    while True:
        mostrar_menu()
        opcion = console.input("Elige una opción (1-6): ").strip()

        if opcion == '1':
            libro_id = console.input("ID del libro a prestar: ").strip()
            nombre = console.input("Nombre del aprendiz que presta: ").strip()
            if libro_id and nombre:
                prestar_libro(libros, libro_id, nombre)

        elif opcion == '2':
            libro_id = console.input("ID del libro a devolver: ").strip()
            if libro_id:
                devolver_libro(libros, libro_id)

        elif opcion == '3':
            query = console.input("Escribe parte del título a buscar: ").strip()
            if query:
                resultados = buscar_libro(libros, query)
                mostrar_tabla_libros(resultados, f"Resultados de Búsqueda: '{query}'")

        elif opcion == '4':
            prestados = ver_libros_prestados(libros)
            mostrar_tabla_libros(prestados, "Libros Actualmente Prestados")

        elif opcion == '5':
            mostrar_tabla_libros(libros, "Inventario Completo de la Biblioteca")

        elif opcion == '6':
            console.print("[bold red]¡Gracias por usar la Biblioteca! ¡Hasta pronto![/bold red]")
            break

        else:
            console.print("[bold red]Opción inválida.[/bold red] Por favor, selecciona un número entre 1 y 6.")


if __name__ == "__main__":
    main()