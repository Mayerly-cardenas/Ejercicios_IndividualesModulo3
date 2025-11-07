from functools import reduce
from typing import List

def suma_numeros(numeros: List[int]) -> int:
    """
    Calcula la suma total de una lista de números usando reduce.
    Devuelve 0 si la lista está vacía.

    Args:
        numeros (List[int]): Lista de números enteros.

    Returns:
        int: Suma total de los números.
    """
    return reduce(lambda a, b: a + b, numeros, 0)  # Valor inicial 0

def concatenar_strings(strings: List[str]) -> str:
    """
    Concatenar una lista de strings en una sola cadena usando reduce.
    Devuelve cadena vacía si la lista está vacía.

    Args:
        strings (List[str]): Lista de strings.

    Returns:
        str: Cadena concatenada.
    """
    return reduce(lambda a, b: a + b, strings, "")  # Valor inicial ""

def main():
    """
    Función principal para probar suma y concatenación con reduce.
    """
    numeros = [1, 2, 3, 4, 5]
    frase = ["Hola", " ", "SENA", "!"]

    print("Suma de números:", suma_numeros(numeros))
    print("Concatenación de strings:", concatenar_strings(frase))

if __name__ == "__main__":
    main()
