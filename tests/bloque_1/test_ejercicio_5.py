from src.bloque_1.ejercicio_5 import calcular_iva, actualizar_tasa_iva, TASA_IVA


def test_calcular_iva_default():
    precio = 100
    # IVA por defecto 19%
    assert calcular_iva(precio) == 100 * 0.19


def test_actualizar_tasa_iva():
    # Guardar tasa original
    tasa_original = TASA_IVA
    actualizar_tasa_iva(0.21)

    # Verificar que calcular_iva refleje la nueva tasa
    assert calcular_iva(100) == 100 * 0.21

    # Restaurar tasa original para no afectar otras pruebas
    actualizar_tasa_iva(tasa_original)


def test_calcular_iva_despues_de_actualizar():
    actualizar_tasa_iva(0.25)
    assert calcular_iva(200) == 200 * 0.25
    # Restaurar tasa original
    actualizar_tasa_iva(0.19)
