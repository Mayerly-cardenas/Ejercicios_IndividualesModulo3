import csv
from typing import Dict
from rich.console import Console
from rich.table import Table

console = Console()

def analizar_csv(nombre_archivo: str, columna: str) -> Dict[str, float]:
    """
    Analiza una columna numérica de un archivo CSV y devuelve promedio, max y min.
    """
    valores = []

    # Leer el CSV
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            try:
                valor = float(fila[columna])
                valores.append(valor)
            except (ValueError, KeyError):
                continue  # Ignorar filas con datos no válidos o columna inexistente

    if not valores:
        resultado = {"promedio": 0.0, "max": 0.0, "min": 0.0}
    else:
        resultado = {
            "promedio": sum(valores) / len(valores),
            "max": max(valores),
            "min": min(valores)
        }

    # Mostrar resultados en tabla con rich
    tabla = Table(title=f"Análisis de columna: {columna}")
    tabla.add_column("Indicador", justify="center")
    tabla.add_column("Valor", justify="center")

    for k, v in resultado.items():
        tabla.add_row(k, f"{v:.2f}")

    console.print(tabla)
    return resultado
