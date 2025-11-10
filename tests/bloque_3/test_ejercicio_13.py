import json
from src.bloque_3.ejercicio_13 import guardar_inventario, cargar_inventario


def test_guardar_y_cargar_inventario(tmp_path):
    archivo = tmp_path / "inventario.json"
    inventario = [
        {"nombre": "Camisa", "precio": 50000, "cantidad": 10},
        {"nombre": "Pantalón", "precio": 80000, "cantidad": 5},
    ]

    guardar_inventario(archivo, inventario)
    cargado = cargar_inventario(archivo)

    assert cargado == inventario
    with open(archivo, "r", encoding="utf-8") as f:
        data = json.load(f)
        assert len(data) == 2
        assert data[0]["nombre"] == "Camisa"
