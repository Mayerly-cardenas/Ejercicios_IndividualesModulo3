"""Pruebas unitarias para el Ejercicio 1: Calculadora de IMC."""

import pytest
from src.bloque_1.ejercicio_1 import calcular_imc, interpretar_imc


def test_calcular_imc_correcto() -> None:
    """Verifica que el cálculo del IMC sea correcto."""
    resultado = calcular_imc(70, 1.75)
    assert resultado == pytest.approx(22.86, 0.01)


def test_calcular_imc_valores_invalidos() -> None:
    """Verifica que se lance un error si los valores son inválidos."""
    with pytest.raises(ValueError):
        calcular_imc(0, 1.70)
    with pytest.raises(ValueError):
        calcular_imc(70, 0)


def test_interpretar_imc_rangos() -> None:
    """Verifica la interpretación del IMC según los rangos definidos."""
    assert interpretar_imc(17.0) == "Bajo peso"
    assert interpretar_imc(22.0) == "Normal"
    assert interpretar_imc(28.0) == "Sobrepeso"
    assert interpretar_imc(33.0) == "Obesidad"
