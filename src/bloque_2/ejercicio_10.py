from typing import Any

def explorar_estructura(elemento: Any, profundidad: int = 1) -> None:
    """
    Explora recursivamente cualquier estructura de datos anidada e imprime
    los valores no iterables junto a su nivel de profundidad.

    Args:
        elemento (Any): La estructura a explorar (lista, diccionario, tupla, etc.)
        profundidad (int): Nivel actual de profundidad.
    """
    if isinstance(elemento, dict):
        for clave, valor in elemento.items():
            print(f"Explorando clave '{clave}' en profundidad {profundidad}")
            explorar_estructura(valor, profundidad + 1)

    elif isinstance(elemento, (list, tuple, set)):
        for valor in elemento:
            explorar_estructura(valor, profundidad + 1)

    else:
        print(f"Valor: {elemento}, Profundidad: {profundidad}")


def menu_ejercicio_10():
    """
    Menú interactivo para probar el explorador de estructuras recursivo.
    """
    while True:
        print("\n--- Ejercicio 10: Explorador de estructuras de datos ---")
        print("1. Probar con estructura de ejemplo")
        print("2. Ingresar estructura personalizada")
        print("3. Salir al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            estructura = [1, [2, 3], {"a": 4, "b": [5, {"c": 6}]}]
            print("\nExplorando estructura de ejemplo:")
            explorar_estructura(estructura)

        elif opcion == "2":
            print("\nIngrese una estructura en formato Python (por ejemplo: [1, {'a': 2, 'b': [3, 4]}])")
            entrada = input(">>> ")
            try:
                estructura_personalizada = eval(entrada)
                print("\nExplorando estructura personalizada:")
                explorar_estructura(estructura_personalizada)
            except Exception as e:
                print(f"Error: {e}. Asegúrese de ingresar una estructura válida.")

        elif opcion == "3":
            print("Regresando al menú principal...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    menu_ejercicio_10()
