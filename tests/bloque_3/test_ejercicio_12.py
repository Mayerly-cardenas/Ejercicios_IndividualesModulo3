import csv
import os
import pytest
from src.bloque_3.ejercicio_12 import analizar_csv

ARCHIVO_PRUEBA = "test_estudiantes.csv"

@pytest.fixture
def archivo_csv():
    # Crear un CSV de prueba
    with open(ARCHIVO_PRUEBA, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["nombre", "edad", "calificacion"])
        writer.writeheader()
        writer.writerow({"nombre": "Ana", "edad": "20", "calificacion": "85"})
        writer.writerow({"nombre": "Luis", "edad": "22", "calificacion": "90"})
        writer.writerow({"nombre": "Marta", "edad": "21", "calificacion": "95"})
    yield
    # Limpiar archivo después del test
    if os.path.exists(ARCHIVO_PRUEBA):
        os.remove(ARCHIVO_PRUEBA)

def test_analizar_csv(archivo_csv):
    resultado = analizar_csv(ARCHIVO_PRUEBA, "calificacion")
    assert resultado["promedio"] == pytest.approx(90.0)
    assert resultado["max"] == 95.0
    assert resultado["min"] == 85.0

def test_columna_inexistente(archivo_csv):
    resultado = analizar_csv(ARCHIVO_PRUEBA, "inexistente")
    assert resultado == {"promedio": 0.0, "max": 0.0, "min": 0.0}
