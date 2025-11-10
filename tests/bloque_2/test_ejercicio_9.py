from bloque_2.ejercicio_9 import calcular_operaciones

def test_calcular_operaciones():
    resultado = calcular_operaciones()
    assert isinstance(resultado, dict)
    assert resultado["suma_total"] == 15
    assert resultado["frase"] == "Hola SENA!"
