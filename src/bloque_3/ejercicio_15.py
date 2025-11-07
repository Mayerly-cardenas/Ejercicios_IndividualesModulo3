import json
from pathlib import Path
from rich.console import Console
from rich.table import Table
from typing import List, Dict, Optional

console = Console()
ARCHIVO_BIBLIOTECA = Path("biblioteca.json")

def cargar_biblioteca() -> List[Dict]:
    """Carga los libros desde el archivo JSON."""
    if not ARCHIVO_BIBLIOTECA.exists():
        return []
    with open(ARCHIVO_BIBLIOTECA, "r", encoding="utf-8") as f:
        return json.load(f)

def guardar_biblioteca(libros: List[Dict]):
    """Guarda la lista de libros en el archivo JSON."""
    with open(ARCHIVO_BIBLIOTECA, "w", encoding="utf-8") as f:
        json.dump(libros, f, indent=4, ensure_ascii=False)

def prestar_libro(libro_id: str, nombre_aprendiz: str):
    """Marca un libro como prestado a un aprendiz."""
    libros = cargar_biblioteca()
    for libro in libros:
        if libro["libro_id"] == libro_id:
            if libro.get("prestado_a"):
                console.print(f"[red]El libro '{libro['titulo']}' ya está prestado a {libro['prestado_a']}[/red]")
                return
            libro["prestado_a"] = nombre_aprendiz
            guardar_biblioteca(libros)
            console.print(f"[green]Libro '{libro['titulo']}' prestado a {nombre_aprendiz}[/green]")
            return
    console.print(f"[red]No se encontró el libro con ID {libro_id}[/red]")

def devolver_libro(libro_id: str):
    """Marca un libro como disponible."""
    libros = cargar_biblioteca()
    for libro in libros:
        if libro["libro_id"] == libro_id:
            libro["prestado_a"] = None
            guardar_biblioteca(libros)
            console.print(f"[green]Libro '{libro['titulo']}' devuelto correctamente[/green]")
            return
    console.print(f"[red]No se encontró el libro con ID {libro_id}[/red]")

def buscar_libro(query: str) -> List[Dict]:
    """Busca libros por título que contengan el query (case insensitive)."""
    libros = cargar_biblioteca()
    resultados = [libro for libro in libros if query.lower() in libro["titulo"].lower()]
    tabla = Table(title=f"Resultados de búsqueda: '{query}'")
    tabla.add_column("ID", justify="center")
    tabla.add_column("Título", justify="left")
    tabla.add_column("Prestado a", justify="center")
    for libro in resultados:
        tabla.add_row(libro["libro_id"], libro["titulo"], str(libro.get("prestado_a") or "Disponible"))
    console.print(tabla)
    return resultados

def ver_libros_prestados() -> List[Dict]:
    """Muestra todos los libros que están prestados."""
    libros = cargar_biblioteca()
    prestados = [libro for libro in libros if libro.get("prestado_a")]
    tabla = Table(title="Libros Prestados")
    tabla.add_column("ID", justify="center")
    tabla.add_column("Título", justify="left")
    tabla.add_column("Prestado a", justify="center")
    for libro in prestados:
        tabla.add_row(libro["libro_id"], libro["titulo"], libro["prestado_a"])
    console.print(tabla)
    return prestados
