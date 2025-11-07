import os
import pytest
from src.bloque_3.ejercicio_11 import agregar_tarea, ver_tareas, ARCHIVO_TAREAS

@pytest.fixture
def limpiar_archivo():
    """Fixture para limpiar el archivo antes y después de cada test"""
    # Guardamos si existe un archivo real
    if os.path.exists(ARCHIVO_TAREAS):
        os.rename(ARCHIVO_TAREAS, ARCHIVO_TAREAS + ".bak")

    yield  # Ejecuta el test

    # Limpiamos archivo de prueba
    if os.path.exists(ARCHIVO_TAREAS):
        os.remove(ARCHIVO_TAREAS)
    # Restauramos el archivo original si existía
    if os.path.exists(ARCHIVO_TAREAS + ".bak"):
        os.rename(ARCHIVO_TAREAS + ".bak", ARCHIVO_TAREAS)

def test_agregar_y_ver_tareas(limpiar_archivo):
    # Agregamos tareas
    agregar_tarea("Tarea 1")
    agregar_tarea("Tarea 2")

    # Verificamos que las tareas se lean correctamente
    tareas = ver_tareas()
    assert tareas == ["Tarea 1", "Tarea 2"]

def test_ver_tareas_vacio(limpiar_archivo):
    # Si el archivo está vacío, debe retornar lista vacía
    tareas = ver_tareas()
    assert tareas == []
