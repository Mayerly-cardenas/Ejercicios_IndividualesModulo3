import io
import sys
from src.bloque_2.ejercicio_10 import explorar_estructura

def explorar_estructura(elemento, profundidad=0):
    """
    Función recursiva que imprime los valores no-iterables de una estructura
    (listas, tuplas, diccionarios) con su profundidad.
    """
    if isinstance(elemento, dict):
        for valor in elemento.values():
            explorar_estructura(valor, profundidad + 1)
    elif isinstance(elemento, (list, tuple)):
        for item in elemento:
            explorar_estructura(item, profundidad + 1)
    else:
        # Sumamos 1 a profundidad al imprimir para que el nivel base sea 1
        print(f"Valor: {elemento}, Profundidad: {profundidad + 1}")

