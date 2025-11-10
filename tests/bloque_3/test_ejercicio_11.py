import os
import pytest
from bloque_3.ejercicio_11 import agregar_tarea, ver_tareas, RUTA_ARCHIVO


@pytest.fixture(autouse=True)
def limpiar_archivo():
    """Limpia el archivo antes y después de cada test."""
    if os.path.exists(RUTA_ARCHIVO):
        os.remove(RUTA_ARCHIVO)
    yield
    if os.path.exists(RUTA_ARCHIVO):
        os.remove(RUTA_ARCHIVO)


def test_agregar_y_ver_tareas():
    agregar_tarea("Estudiar Python")
    agregar_tarea("Hacer ejercicio")
    tareas = ver_tareas()
    assert len(tareas) == 2
    assert "Estudiar Python" in tareas
    assert "Hacer ejercicio" in tareas


def test_ver_tareas_archivo_vacio():
    tareas = ver_tareas()
    assert tareas == []
