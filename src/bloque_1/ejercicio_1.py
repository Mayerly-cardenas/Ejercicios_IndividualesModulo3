"""
Ejercicio 1: Refactorización de Calculadora de IMC
Autor: Nubia Mayerly Cárdenas Bautista
Programa: Tecnólogo en Análisis y Desarrollo de Software - SENA
"""

from rich.console import Console

console = Console()


def calcular_imc(peso: float, altura: float) -> float:
    """
    Calcula el Índice de Masa Corporal (IMC).

    Args:
        peso (float): Peso de la persona en kilogramos.
        altura (float): Altura de la persona en metros.

    Returns:
        float: Valor del IMC calculado.
    """
    return peso / (altura ** 2)


def interpretar_imc(imc: float) -> str:
    """
    Interpreta el valor del IMC según los rangos estándar de la OMS.

    Args:
        imc (float): Índice de Masa Corporal calculado.

    Returns:
        str: Interpretación del IMC (Bajo peso, Normal, Sobrepeso u Obesidad).
    """
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"


def main() -> None:
    """
    Función principal que solicita datos al usuario, calcula el IMC
    y muestra el resultado en consola usando la librería rich.
    """
    console.print("[bold cyan]=== Calculadora de IMC ===[/bold cyan]")
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))

    imc = calcular_imc(peso, altura)
    interpretacion = interpretar_imc(imc)

    console.print(f"\n[bold green]Su IMC es:[/bold green] {imc:.2f}")
    console.print(f"[bold yellow]Interpretación:[/bold yellow] {interpretacion}")


if __name__ == "__main__":
    main()
