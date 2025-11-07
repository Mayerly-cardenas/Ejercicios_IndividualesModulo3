from src.bloque_1.ejercicio_3 import crear_contador

def test_contadores_independientes():
    contador_a = crear_contador()
    contador_b = crear_contador()

    # Probar que cada contador es independiente
    assert contador_a() == 1
    assert contador_a() == 2
    assert contador_b() == 1
    assert contador_a() == 3
    assert contador_b() == 2

def test_incremento_contador_unico():
    contador = crear_contador()
    assert contador() == 1
    assert contador() == 2
    assert contador() == 3
