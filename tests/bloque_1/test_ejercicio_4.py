import pytest
from src.bloque_1.ejercicio_4 import (
    aplicar_validador,
    es_email_valido,
    es_mayor_a_10
)


def test_es_email_valido():
    assert es_email_valido("usuario@gmail.com") is True
    assert es_email_valido("usuario@dominio.com") is True
    assert es_email_valido("usuario@dominio") is False
    assert es_email_valido("usuariodominio.com") is False
    assert es_email_valido("") is False


def test_es_mayor_a_10():
    assert es_mayor_a_10(11) is True
    assert es_mayor_a_10(100) is True
    assert es_mayor_a_10(10) is False
    assert es_mayor_a_10(0) is False
    assert es_mayor_a_10(-5) is False


def test_aplicar_validador_emails():
    datos = ["correo@gmail.com", "test@", "sin_arroba.com"]
    resultado = aplicar_validador(datos, es_email_valido)
    assert resultado == ["correo@gmail.com"]


def test_aplicar_validador_numeros():
    datos = [5, 12, 8, 20]
    resultado = aplicar_validador(datos, es_mayor_a_10)
    assert resultado == [12, 20]
