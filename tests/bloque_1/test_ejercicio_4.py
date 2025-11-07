from src.bloque_1.ejercicio_4 import aplicar_validador, es_email_valido, es_mayor_a_10

def test_aplicar_validador_emails():
    datos = ["a@b.com", "mal", "user@example.com"]
    resultado = aplicar_validador(datos, es_email_valido)
    assert resultado == ["a@b.com", "user@example.com"]

def test_aplicar_validador_numeros():
    numeros = [5, 12, 3, 20]
    resultado = aplicar_validador(numeros, es_mayor_a_10)
    assert resultado == [12, 20]

def test_es_email_valido_true():
    assert es_email_valido("usuario@mail.com") is True

def test_es_email_valido_false():
    assert es_email_valido("usuario-mail.com") is False

def test_es_mayor_a_10_true():
    assert es_mayor_a_10(15) is True

def test_es_mayor_a_10_false():
    assert es_mayor_a_10(5) is False
