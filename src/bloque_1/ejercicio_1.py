"""Ejercicio 1: Calculadora de IMC.

Este módulo calcula el Índice de Masa Corporal (IMC) siguiendo el principio
de responsabilidad única y aplicando buenas prácticas de documentación,
tipado y estilo.
"""

from rich.console import Console
from rich.table import Table


def calcular_imc(peso: float, altura: float) -> float:
    """Calcula el Índice de Masa Corporal (IMC).

    Args:
        peso (float): Peso de la persona en kilogramos.
        altura (float): Altura de la persona en metros.

    Returns:
        float: Valor del IMC redondeado a dos decimales.

    Raises:
        ValueError: Si el peso o la altura son menores o iguales a cero.
    """
    if peso <= 0 or altura <= 0:
        raise ValueError("El peso y la altura deben ser mayores que cero.")
    return round(peso / (altura ** 2), 2)


def interpretar_imc(imc: float) -> str:
    """Interpreta el IMC según los rangos estándar de la OMS.

    Args:
        imc (float): Valor del índice de masa corporal.

    Returns:
        str: Clasificación correspondiente al valor del IMC.
    """
    if imc < 18.5:
        return "Bajo peso"
    if imc < 25:
        return "Normal"
    if imc < 30:
        return "Sobrepeso"
    return "Obesidad"


def mostrar_resultado(peso: float, altura: float, imc: float, interpretacion: str) -> None:
    """Muestra los resultados del cálculo de IMC con Rich.

    Args:
        peso (float): Peso del usuario.
        altura (float): Altura del usuario.
        imc (float): Valor del IMC calculado.
        interpretacion (str): Categoría del IMC.
    """
    consola = Console()
    tabla = Table(title="Resultado del Cálculo de IMC")

    tabla.add_column("Dato", justify="center", style="bold cyan")
    tabla.add_column("Valor", justify="center", style="bold green")

    tabla.add_row("Peso (kg)", f"{peso}")
    tabla.add_row("Altura (m)", f"{altura}")
    tabla.add_row("IMC", f"{imc}")
    tabla.add_row("Interpretación", interpretacion)

    consola.print(tabla)


def main() -> None:
    """Función principal que orquesta el cálculo del IMC."""
    consola = Console()
    consola.print("[bold magenta]Calculadora de IMC[/bold magenta]\n")

    try:
        peso = float(input("Ingrese su peso en kilogramos: "))
        altura = float(input("Ingrese su altura en metros: "))

        imc = calcular_imc(peso, altura)
        interpretacion = interpretar_imc(imc)
        mostrar_resultado(peso, altura, imc, interpretacion)

    except ValueError as error:
        consola.print(f"[bold red]Error:[/bold red] {error}")


if __name__ == "__main__":
    main()
