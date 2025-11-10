from functools import reduce

def calcular_operaciones():
    """
    Utiliza functools.reduce para realizar dos operaciones:
    1. Calcular la suma total de una lista de números.
    2. Concatenar una lista de strings en una sola frase.

    Returns:
        dict: Un diccionario con la suma total y la frase concatenada.
    """
    numeros = [1, 2, 3, 4, 5]
    palabras = ["Hola", " ", "SENA", "!"]

    # Calcular la suma total usando reduce
    suma_total = reduce(lambda x, y: x + y, numeros)

    # Concatenar palabras usando reduce
    frase_concatenada = reduce(lambda x, y: x + y, palabras)

    return {
        "suma_total": suma_total,
        "frase": frase_concatenada
    }


def mostrar_resultados(resultados):
    """
    Muestra los resultados obtenidos en consola.
    """
    print(f"Suma total: {resultados['suma_total']}")
    print(f"Frase concatenada: {resultados['frase']}")


def menu_ejercicio_9():
    """
    Menú principal para ejecutar el ejercicio 9.
    """
    while True:
        print("\n--- Ejercicio 9: Operaciones con reduce ---")
        print("1. Calcular operaciones")
        print("2. Salir al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            resultados = calcular_operaciones()
            mostrar_resultados(resultados)
        elif opcion == "2":
            print("Regresando al menú principal...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    menu_ejercicio_9()
