from bloque_2.ejercicio_8 import obtener_palabras_largas, contar_longitudes


def test_obtener_palabras_largas_basico():
    texto = "La programación en Python es maravillosa y poderosa"
    resultado = obtener_palabras_largas(texto)
    assert "PROGRAMACIÓN" in resultado
    assert "MARAVILLOSA" in resultado
    assert "PODEROSA" in resultado
    assert "PYTHON" not in resultado


def test_contar_longitudes_correctas():
    palabras = ["PROGRAMACIÓN", "MARAVILLOSA"]
    resultado = contar_longitudes(palabras)
    assert resultado == {"PROGRAMACIÓN": 12, "MARAVILLOSA": 11}


def test_palabras_largas_vacias():
    texto = "sol luz mar pez"
    resultado = obtener_palabras_largas(texto)
    assert resultado == []
