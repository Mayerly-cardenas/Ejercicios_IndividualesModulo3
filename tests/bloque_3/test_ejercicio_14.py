import pytest
import os
import tempfile
import json
import csv
# ¡Línea de importación clave! Asegúrate de que tu archivo en src se llame ejercicio14.py
from src.bloque_3.ejercicio_14 import leer_csv, leer_json, generar_reporte

# Datos de prueba para crear archivos temporales
TEST_CSV_DATA = [
    {"id_estudiante": "101", "nombre": "Ana Pérez", "id_cursos": "M1, F2"},
    {"id_estudiante": "102", "nombre": "Juan López", "id_cursos": "M1"},
    {"id_estudiante": "103", "nombre": "Marta Diaz", "id_cursos": ""},
]

TEST_JSON_DATA = {
    "M1": "Matemáticas I",
    "F2": "Física II",
    "P3": "Programación Avanzada"
}


@pytest.fixture
def archivos_temporales():
    """Crea archivos temporales CSV y JSON para las pruebas."""
    temp_dir = tempfile.mkdtemp()

    # 1. Crear CSV de estudiantes
    csv_path = os.path.join(temp_dir, "estudiantes_test.csv")
    with open(csv_path, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["id_estudiante", "nombre", "id_cursos"])
        writer.writeheader()
        writer.writerows(TEST_CSV_DATA)

    # 2. Crear JSON de cursos
    json_path = os.path.join(temp_dir, "cursos_test.json")
    with open(json_path, mode='w', encoding='utf-8') as f:
        json.dump(TEST_JSON_DATA, f)

    yield csv_path, json_path

    # Limpieza
    try:
        os.remove(csv_path)
        os.remove(json_path)
        os.rmdir(temp_dir)
    except Exception:
        pass


def test_leer_csv_correcto(archivos_temporales):
    """Verifica que leer_csv cargue correctamente los datos y separe los IDs de cursos."""
    csv_path, _ = archivos_temporales
    datos = leer_csv(csv_path)

    assert len(datos) == 3
    assert datos[0]['nombre'] == 'Ana Pérez'
    assert datos[0]['cursos'] == ['M1', 'F2']


def test_leer_csv_no_encontrado():
    """Verifica el manejo de archivo no encontrado."""
    datos = leer_csv("ruta/invalida/no_existe.csv")
    assert datos == []


def test_generar_reporte_contenido():
    """Verifica que el reporte genere el contenido esperado combinando datos."""
    estudiantes_data = [
        {"id_estudiante": "1", "nombre": "Luisa", "cursos": ["C1", "C2"]},
        {"id_estudiante": "2", "nombre": "Pedro", "cursos": []},
    ]
    cursos_data = {"C1": "Cloud", "C2": "Backend"}

    reporte = generar_reporte(estudiantes_data, cursos_data)

    assert "**Luisa**" in reporte
    assert "- Cloud" in reporte
    assert "**Pedro**" in reporte
    assert "*No tiene cursos inscritos.*" in reporte