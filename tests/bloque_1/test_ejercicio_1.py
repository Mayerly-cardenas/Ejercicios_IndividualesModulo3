from src.bloque_1.ejercicio_1 import calcular_imc, interpretar_imc


def test_calcular_imc():
    assert round(calcular_imc(70, 1.75), 2) == 22.86
    assert round(calcular_imc(50, 1.60), 2) == 19.53


def test_interpretar_imc():
    assert interpretar_imc(17.5) == "Bajo peso"
    assert interpretar_imc(22.0) == "Peso normal"
    assert interpretar_imc(27.5) == "Sobrepeso"
    assert interpretar_imc(31.0) == "Obesidad"
