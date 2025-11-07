import os
import pytest
from src.bloque_3 import ejercicio_15 as bib

ARCHIVO_PRUEBA = "biblioteca.json"

@pytest.fixture(autouse=True)
def setup_archivo():
    # Crear archivo JSON de prueba
    libros_prueba = [
        {"libro_id": "001", "titulo": "Cien Años de Soledad", "prestado_a": None},
        {"libro_id": "002", "titulo": "Don Quijote", "prestado_a": None}
    ]
    with open(ARCHIVO_PRUEBA, "w", encoding="utf-8") as f:
        import json
        json.dump(libros_prueba, f)

    yield

    # Limpiar después del test
    if os.path.exists(ARCHIVO_PRUEBA):
        os.remove(ARCHIVO_PRUEBA)

def test_prestar_y_devolver_libro(capsys):
    bib.prestar_libro("001", "Alice")
    libros = bib.cargar_biblioteca()
    assert libros[0]["prestado_a"] == "Alice"

    bib.devolver_libro("001")
    libros = bib.cargar_biblioteca()
    assert libros[0]["prestado_a"] is None

def test_buscar_libro(capsys):
    resultados = bib.buscar_libro("Cien Años")
    assert len(resultados) == 1
    assert resultados[0]["titulo"] == "Cien Años de Soledad"

def test_ver_libros_prestados(capsys):
    bib.prestar_libro("002", "Bob")
    prestados = bib.ver_libros_prestados()
    assert len(prestados) == 1
    assert prestados[0]["prestado_a"] == "Bob"
