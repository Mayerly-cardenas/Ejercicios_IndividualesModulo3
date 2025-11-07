import os
import pytest
from src.bloque_3 import ejercicio_14 as rep

CSV_PRUEBA = "estudiantes.csv"
JSON_PRUEBA = "cursos.json"
REPORTE_PRUEBA = "reporte.txt"

@pytest.fixture(autouse=True)
def setup_archivos():
    # Crear archivos de prueba
    with open(CSV_PRUEBA, "w", encoding="utf-8") as f:
        f.write("nombre,cursos\nAlice,1,2\nBob,2,3\n")

    cursos_data = {
        "1": {"nombre": "Matemáticas"},
        "2": {"nombre": "Física"},
        "3": {"nombre": "Química"}
    }
    with open(JSON_PRUEBA, "w", encoding="utf-8") as f:
        import json
        json.dump(cursos_data, f)

    yield

    # Limpiar archivos después del test
    for archivo in [CSV_PRUEBA, JSON_PRUEBA, REPORTE_PRUEBA]:
        if os.path.exists(archivo):
            os.remove(archivo)

def test_generar_reporte(capsys):
    estudiantes = rep.leer_csv(CSV_PRUEBA)
    cursos = rep.leer_json(JSON_PRUEBA)
    rep.generar_reporte(estudiantes, cursos, REPORTE_PRUEBA)

    # Revisar que el archivo se creó
    assert os.path.exists(REPORTE_PRUEBA)

    # Capturar salida en consola
    captured = capsys.readouterr()
    assert "Reporte de Estudiantes y Cursos" in captured.out
    assert "Alice" in captured.out
    assert "Matemáticas" in captured.out
