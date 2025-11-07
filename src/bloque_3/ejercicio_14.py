import csv
import json
from rich.console import Console

console = Console()

def leer_csv(nombre_archivo: str) -> list[dict]:
    """Lee un archivo CSV y devuelve una lista de diccionarios."""
    estudiantes = []
    with open(nombre_archivo, "r", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        for fila in lector:
            estudiantes.append(fila)
    return estudiantes

def leer_json(nombre_archivo: str) -> dict:
    """Lee un archivo JSON y devuelve su contenido."""
    with open(nombre_archivo, "r", encoding="utf-8") as f:
        return json.load(f)

def generar_reporte(estudiantes: list[dict], cursos: dict, archivo_salida: str):
    """Genera un reporte indicando qué cursos ha tomado cada estudiante."""
    lineas = []
    for estudiante in estudiantes:
        nombre = estudiante.get("nombre")
        ids_cursos = estudiante.get("cursos", "").split(",")  # separar IDs si vienen en cadena
        cursos_tomados = [cursos[cid]["nombre"] for cid in ids_cursos if cid in cursos]
        linea = f"{nombre}: {', '.join(cursos_tomados)}"
        lineas.append(linea)

    # Mostrar reporte en consola
    console.print("\n[bold green]Reporte de Estudiantes y Cursos[/bold green]")
    for linea in lineas:
        console.print(linea)

    # Guardar reporte en archivo
    with open(archivo_salida, "w", encoding="utf-8") as f:
        f.write("\n".join(lineas))
