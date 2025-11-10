from typing import Callable, Any


def aplicar_validador(datos: list[Any], validador: Callable[[Any], bool]) -> list[Any]:
    """
    Aplica una función validadora a cada elemento de la lista y devuelve solo los válidos.

    Args:
        datos (list[Any]): Lista de elementos a validar.
        validador (Callable[[Any], bool]): Función que recibe un elemento y devuelve True o False.

    Returns:
        list[Any]: Nueva lista con los elementos que pasaron la validación.
    """
    return [elemento for elemento in datos if validador(elemento)]


def es_email_valido(email: str) -> bool:
    """
    Verifica si un email tiene un formato válido básico (contiene '@' y un punto).

    Args:
        email (str): Dirección de correo a validar.

    Returns:
        bool: True si el formato es válido, False en caso contrario.
    """
    return "@" in email and "." in email


def es_mayor_a_10(numero: int) -> bool:
    """
    Verifica si un número es mayor que 10.

    Args:
        numero (int): Número a evaluar.

    Returns:
        bool: True si el número es mayor que 10, False en caso contrario.
    """
    return numero > 10


def mostrar_menu():
    """Muestra el menú principal."""
    print("\n===  VALIDADOR DE DATOS ===")
    print("1. Validar correos electrónicos")
    print("2. Validar números mayores a 10")
    print("3. Salir")


def validar_correos():
    """Permite validar correos ingresados por el usuario."""
    correos = input("\nIngrese los correos separados por coma: ").split(",")
    correos = [c.strip() for c in correos]
    resultado = aplicar_validador(correos, es_email_valido)
    print("\n Correos válidos:")
    print(resultado if resultado else "Ninguno válido.")


def validar_numeros():
    """Permite validar números ingresados por el usuario."""
    numeros_str = input("\nIngrese los números separados por coma: ").split(",")
    try:
        numeros = [int(n.strip()) for n in numeros_str]
    except ValueError:
        print(" Error: Todos los valores deben ser números.")
        return
    resultado = aplicar_validador(numeros, es_mayor_a_10)
    print("\n Números mayores a 10:")
    print(resultado if resultado else "Ninguno válido.")


def main():
    """Función principal que controla el flujo del programa con menú repetitivo."""
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-3): ").strip()

        if opcion == "1":
            validar_correos()
        elif opcion == "2":
            validar_numeros()
        elif opcion == "3":
            print("\n Gracias por usar el validador. Hasta pronto")
            break
        else:
            print(" Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()
