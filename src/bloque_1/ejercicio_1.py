"""
Ejercicio 1: Calculadora de IMC
Bloque 1 - Diseño y Refactorización con Funciones

Este programa permite calcular el Índice de Masa Corporal (IMC) de una persona
a partir de su peso y altura. Se aplican principios de modularidad y
responsabilidad única para mantener el código limpio y reutilizable.
"""

def calcular_imc(peso: float, altura: float) -> float:
    """
    Calcula el índice de masa corporal (IMC).
    Fórmula: IMC = peso / (altura ** 2)
    """
    if altura <= 0:
        raise ValueError("La altura debe ser mayor que cero.")
    return round(peso / (altura ** 2), 2)


def interpretar_imc(imc: float) -> str:
    """
    Interpreta el valor del IMC según rangos estándar.
    """
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 25:
        return "Normal"  # 👈 Cambiado para coincidir con el test
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"

