from src.bloque_1.ejercicio_5 import calcular_iva, actualizar_tasa_iva, TASA_IVA


def test_calcular_iva_valor_por_defecto():
    precio = 1000
    iva = calcular_iva(precio)
    assert round(iva, 2) == round(precio * TASA_IVA, 2)


def test_actualizar_tasa_iva_modifica_valor():
    actualizar_tasa_iva(0.10)
    assert abs(calcular_iva(1000) - 100) < 0.01

    actualizar_tasa_iva(0.19)  # Restauramos el valor original
    assert abs(calcular_iva(1000) - 190) < 0.01
