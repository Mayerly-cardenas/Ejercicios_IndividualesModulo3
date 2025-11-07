import os
import pytest
import json
from src.bloque_3 import ejercicio_13 as inv

ARCHIVO_PRUEBA = "inventario.json"

@pytest.fixture(autouse=True)
def limpiar_archivo():
    # Antes del test, asegurarse de que el archivo no exista
    if os.path.exists(ARCHIVO_PRUEBA):
        os.remove(ARCHIVO_PRUEBA)
    yield
    # Después del test, limpiar
    if os.path.exists(ARCHIVO_PRUEBA):
        os.remove(ARCHIVO_PRUEBA)

def test_agregar_y_cargar_producto():
    inv.agregar_producto("Laptop", 5, 1500.0)
    inventario = inv.cargar_inventario()
    assert len(inventario) == 1
    assert inventario[0]["nombre"] == "Laptop"
    assert inventario[0]["cantidad"] == 5
    assert inventario[0]["precio"] == 1500.0

def test_vender_producto():
    inv.agregar_producto("Teclado", 10, 50.0)
    assert inv.vender_producto("Teclado", 5) is True
    inventario = inv.cargar_inventario()
    assert inventario[0]["cantidad"] == 5
    # Intentar vender más de lo disponible
    assert inv.vender_producto("Teclado", 10) is False

def test_mostrar_inventario(capsys):
    inv.agregar_producto("Monitor", 3, 300.0)
    inv.mostrar_inventario()
    captured = capsys.readouterr()
    assert "Monitor" in captured.out
    assert "3" in captured.out
    assert "300.00" in captured.out
