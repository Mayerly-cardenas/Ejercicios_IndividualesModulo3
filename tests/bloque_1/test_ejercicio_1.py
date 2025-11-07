from src.bloque_1.ejercicio_1 import calcular_imc, interpretar_imc


def test_calcular_imc():
    assert calcular_imc(70, 1.75) == 22.86


def test_interpretar_imc():
    assert interpretar_imc(22.86) == "Normal"
    assert interpretar_imc(17.5) == "Bajo peso"
    assert interpretar_imc(27.0) == "Sobrepeso"
    assert interpretar_imc(32.0) == "Obesidad"
