from io import StringIO
from unittest.mock import patch
from bloque_2.ejercicio_6 import tienda_ropa


def test_descuento_aplicado(monkeypatch):
    inputs = iter(["2", "5"])  # Aplicar descuento y luego salir
    with patch("builtins.input", lambda _: next(inputs)):
        with patch("sys.stdout", new=StringIO()) as output:
            tienda_ropa()
            salida = output.getvalue()
            assert "Aplicando descuento del 10%" in salida
            assert "Productos con descuento" in salida

def test_eliminar_producto(monkeypatch):
    inputs = iter(["3", "Camisa", "5"])  # Eliminar producto y salir
    with patch("builtins.input", lambda _: next(inputs)):
        with patch("sys.stdout", new=StringIO()) as output:
            tienda_ropa()
            salida = output.getvalue()
            assert "Producto 'Camisa' eliminado exitosamente" in salida

def test_compra(monkeypatch):
    inputs = iter(["4", "Camisa", "Fin", "5"])  # Comprar un producto y salir
    with patch("builtins.input", lambda _: next(inputs)):
        with patch("sys.stdout", new=StringIO()) as output:
            tienda_ropa()
            salida = output.getvalue()
            assert "Resumen de compra" in salida
            assert "Total a pagar" in salida
