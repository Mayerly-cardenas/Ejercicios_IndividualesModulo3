"""
Ejercicio 8: Transformación de Datos con List y Dictionary Comprehensions

Este programa recibe un texto y:
1. Crea una lista con las palabras de más de 5 letras en mayúsculas.
2. Crea un diccionario con la longitud de cada palabra de esa lista.

Conceptos aplicados:
- List comprehensions
- Dictionary comprehensions
- Métodos de strings (split, upper)
"""

from typing import List, Dict


def obtener_palabras_largas(texto: str) -> list:
    palabras = texto.split()
    # Filtramos las que tengan más de 5 letras y NO empiecen con mayúscula
    return [p.upper() for p in palabras if len(p) > 5 and not p[0].isupper()]

    """
    Retorna las palabras con más de 5 letras en mayúsculas.

    Args:
        texto (str): Texto ingresado por el usuario.

    Returns:
        List[str]: Lista de palabras en mayúsculas con más de 5 letras.
    """
    return [palabra.upper() for palabra in texto.split() if len(palabra) > 5]


def contar_longitudes(palabras: List[str]) -> Dict[str, int]:
    """
    Retorna un diccionario con las palabras y su longitud.

    Args:
        palabras (List[str]): Lista de palabras.

    Returns:
        Dict[str, int]: Diccionario con palabra y número de letras.
    """
    return {palabra: len(palabra) for palabra in palabras}


def menu_transformacion_texto() -> None:
    """Muestra un menú interactivo para ingresar texto y aplicar las transformaciones."""
    texto = ""

    while True:
        print("\nMENÚ TRANSFORMACIÓN DE TEXTO")
        print("1. Ingresar texto nuevo")
        print("2. Ver palabras largas en mayúsculas (>5 letras)")
        print("3. Ver diccionario con longitudes de palabras")
        print("4. Salir al menú principal")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            texto = input("\nIngresa o pega el texto: ")
            print("Texto guardado correctamente.")

        elif opcion == "2":
            if texto:
                palabras = obtener_palabras_largas(texto)
                if palabras:
                    print("\nPalabras con más de 5 letras en MAYÚSCULAS:")
                    print(", ".join(palabras))
                else:
                    print("No hay palabras de más de 5 letras.")
            else:
                print("Primero debes ingresar un texto.")

        elif opcion == "3":
            if texto:
                palabras = obtener_palabras_largas(texto)
                longitudes = contar_longitudes(palabras)
                if longitudes:
                    print("\nLongitud de palabras encontradas:")
                    for palabra, longitud in longitudes.items():
                        print(f"- {palabra}: {longitud} letras")
                else:
                    print("No hay palabras que analizar.")
            else:
                print("Primero debes ingresar un texto.")

        elif opcion == "4":
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    menu_transformacion_texto()
