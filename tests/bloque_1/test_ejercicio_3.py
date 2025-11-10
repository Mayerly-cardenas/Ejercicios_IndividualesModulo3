from src.bloque_1.ejercicio_3 import crear_contador


def test_contador_independiente():
    contador_a = crear_contador()
    contador_b = crear_contador()

    # Cada contador debe tener su propio conteo independiente
    assert contador_a() == 1
    assert contador_a() == 2
    assert contador_b() == 1
    assert contador_b() == 2
    assert contador_a() == 3


def test_incremento_correcto():
    contador = crear_contador()
    resultados = [contador() for _ in range(5)]
    assert resultados == [1, 2, 3, 4, 5]
