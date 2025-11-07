from typing import List, Dict


def palabras_mayusculas_largas(texto: str) -> list[str]:
    """
    Devuelve una lista de palabras en mayúsculas y con más de 6 letras
    de un texto dado.

    Args:
        texto (str): Texto de entrada.

    Returns:
        List[str]: Lista de palabras en mayúsculas y largas.
    """
    palabras = texto.split()
    return [palabra for palabra in palabras if palabra.isupper() and len(palabra) > 6]


def longitud_palabras(palabras: List[str]) -> Dict[str, int]:
    """
    Crea un diccionario que asocia cada palabra con su longitud.

    Args:
        palabras (List[str]): Lista de palabras.

    Returns:
        Dict[str, int]: Diccionario {palabra: longitud}.
    """
    return {palabra: len(palabra) for palabra in palabras}


def main():
    """
    Función principal para probar las comprehensions con un texto.
    """
    texto = "ESTO es un EJEMPLO de TEXTO con PALABRAS MAYUSCULAS y algunas CORTAS"
    palabras_filtradas = palabras_mayusculas_largas(texto)
    diccionario_longitudes = longitud_palabras(palabras_filtradas)

    print("Palabras filtradas:", palabras_filtradas)
    print("Diccionario de longitudes:", diccionario_longitudes)


if __name__ == "__main__":
    main()
