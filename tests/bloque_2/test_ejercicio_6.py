from src.bloque_2.ejercicio_6 import aplicar_descuento

def test_aplicar_descuento_default():
    productos = [
        {"nombre": "Camisa", "precio": 50000},
        {"nombre": "Pantalón", "precio": 80000},
        {"nombre": "Zapatos", "precio": 120000},
    ]
    resultado = aplicar_descuento(productos)
    assert resultado == [45000.0, 72000.0, 108000.0]

def test_aplicar_descuento_personalizado():
    productos = [
        {"nombre": "Camisa", "precio": 100},
        {"nombre": "Pantalón", "precio": 200},
    ]
    resultado = aplicar_descuento(productos, descuento=0.20)  # 20% de descuento
    assert resultado == [80.0, 160.0]

def test_aplicar_descuento_precio_decimal():
    productos = [{"nombre": "Calcetines", "precio": 55.5}]
    resultado = aplicar_descuento(productos)
    assert resultado == [49.95]
