import csv
import json
from rich.console import Console
import os

# --- RUTAS DE ARCHIVOS (Relativas a la carpeta de ejecución, la raíz del proyecto) ---
CSV_FILE = "estudiantes.csv"
JSON_FILE = "cursos.json"
REPORT_FILE = "reporte.txt"


# --- FUNCIONES DE CREACIÓN DE ARCHIVOS DE EJEMPLO ---

def crear_csv_ejemplo(ruta_archivo: str):
    """Crea un archivo CSV de ejemplo si no existe."""
    if os.path.exists(ruta_archivo):
        return

    csv_data = [
        {"id_estudiante": "101", "nombre": "Ana Pérez", "id_cursos": "M1, F2"},
        {"id_estudiante": "102", "nombre": "Juan López", "id_cursos": "M1"},
        {"id_estudiante": "103", "nombre": "Marta Diaz", "id_cursos": ""},
        {"id_estudiante": "104", "nombre": "Ricardo Gómez", "id_cursos": "P3, F2"},
    ]

    try:
        with open(ruta_archivo, mode='w', newline='', encoding='utf-8') as archivo:
            fieldnames = ["id_estudiante", "nombre", "id_cursos"]
            writer = csv.DictWriter(archivo, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(csv_data)
        print(f"📄 Creado archivo de ejemplo: {ruta_archivo}")
    except IOError as e:
        print(f"Error al crear el CSV de ejemplo: {e}")


def crear_json_ejemplo(ruta_archivo: str):
    """Crea un archivo JSON de ejemplo si no existe."""
    if os.path.exists(ruta_archivo):
        return

    json_data = {
        "M1": "Matemáticas I",
        "F2": "Física II",
        "P3": "Programación Avanzada",
        "H4": "Historia del Arte"
    }

    try:
        with open(ruta_archivo, mode='w', encoding='utf-8') as archivo:
            json.dump(json_data, archivo, indent=4)
        print(f"📄 Creado archivo de ejemplo: {ruta_archivo}")
    except IOError as e:
        print(f"Error al crear el JSON de ejemplo: {e}")


# --- LÓGICA DEL EJERCICIO ---

def leer_csv(ruta_archivo: str) -> list:
    """Lee el archivo CSV de estudiantes y devuelve una lista de diccionarios."""
    datos = []
    try:
        with open(ruta_archivo, mode='r', newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                if 'id_cursos' in fila and fila['id_cursos']:
                    fila['cursos'] = [c.strip() for c in fila['id_cursos'].split(',')]
                else:
                    fila['cursos'] = []
                # Solo incluimos las claves necesarias para el reporte
                datos.append({
                    'id_estudiante': fila.get('id_estudiante'),
                    'nombre': fila.get('nombre'),
                    'cursos': fila.get('cursos', [])
                })
        return datos
    except FileNotFoundError:
        return []


def leer_json(ruta_archivo: str) -> dict:
    """Lee el archivo JSON de cursos y devuelve un diccionario de {id: nombre}."""
    try:
        with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}


def generar_reporte(estudiantes: list, cursos: dict) -> str:
    """Combina la información y genera el contenido del reporte como un string."""
    reporte_contenido = "================== REPORTE DE MATRÍCULAS ==================\n\n"

    if not estudiantes:
        return reporte_contenido + "No se encontraron datos de estudiantes para generar el reporte."

    for estudiante in estudiantes:
        nombre_estudiante = estudiante.get('nombre', 'Estudiante Desconocido')
        id_cursos_tomados = estudiante.get('cursos', [])

        # Usamos ** para que rich lo muestre en negrita
        reporte_contenido += f"Estudiante: **{nombre_estudiante}** (ID: {estudiante.get('id_estudiante', 'N/A')})\n"

        if id_cursos_tomados:
            reporte_contenido += "Cursos Inscritos:\n"

            for id_curso in id_cursos_tomados:
                nombre_curso = cursos.get(id_curso, f"Curso Desconocido (ID: {id_curso})")
                reporte_contenido += f"  - {nombre_curso}\n"
        else:
            reporte_contenido += "  *No tiene cursos inscritos.*\n"

        reporte_contenido += "---------------------------------------------------------\n"

    return reporte_contenido


def ejecutar_reporte(csv_path: str, json_path: str, reporte_path: str):
    """Función principal que orquesta el proceso y verifica/crea archivos."""

    # 1. Verificar y crear archivos de datos de ejemplo si no existen
    crear_csv_ejemplo(csv_path)
    crear_json_ejemplo(json_path)

    # 2. Leer datos
    datos_estudiantes = leer_csv(csv_path)
    datos_cursos = leer_json(json_path)

    if not datos_estudiantes or not datos_cursos:
        print("Proceso abortado debido a errores de lectura o datos vacíos.")
        return

    # 3. Generar el contenido del reporte
    reporte_final = generar_reporte(datos_estudiantes, datos_cursos)

    # 4. Guardar el reporte
    try:
        with open(reporte_path, mode='w', encoding='utf-8') as f:
            f.write(reporte_final)
        print(f"\n✅ Reporte generado y guardado exitosamente en: {reporte_path}")
    except IOError:
        print(f"Error: No se pudo escribir el archivo en {reporte_path}")
        return

    # 5. Mostrar el reporte en consola con rich
    print("\n================== REPORTE EN CONSOLA (rich) ==================\n")
    console = Console()
    # Muestra el reporte con formato usando rich
    console.print(reporte_final)
    print("\n===============================================================\n")


if __name__ == "__main__":
    ejecutar_reporte(CSV_FILE, JSON_FILE, REPORT_FILE)