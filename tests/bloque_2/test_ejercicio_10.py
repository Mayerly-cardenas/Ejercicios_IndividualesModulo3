from bloque_2.ejercicio_10 import explorar_estructura

def test_explorar_estructura(capsys):
    estructura = [1, [2, 3], {"a": 4}]
    explorar_estructura(estructura)
    salida = capsys.readouterr().out

    assert "Valor: 1, Profundidad: 2" in salida
    assert "Valor: 2, Profundidad: 3" in salida
    assert "Valor: 3, Profundidad: 3" in salida
    assert "Valor: 4, Profundidad: 3" in salida
