from typing import Callable, List


def aplicar_validador(datos: List, validador: Callable) -> List:
    """
    Aplica una función validadora a cada elemento de una lista y devuelve
    una nueva lista con los elementos que pasan la validación.

    Args:
        datos (List): Lista de datos a validar.
        validador (Callable): Función que retorna True si el elemento es válido.

    Returns:
        List: Lista con los elementos que pasaron la validación.
    """
    return [dato for dato in datos if validador(dato)]


def es_email_valido(email: str) -> bool:
    """
    Valida si un string tiene un formato básico de email (contiene '@' y '.').

    Args:
        email (str): String a validar como email.

    Returns:
        bool: True si es un email válido, False si no.
    """
    return "@" in email and "." in email


def es_mayor_a_10(numero: int) -> bool:
    """
    Valida si un número es mayor a 10.

    Args:
        numero (int): Número a validar.

    Returns:
        bool: True si el número es mayor a 10, False si no.
    """
    return numero > 10


def main():
    """
    Función principal para probar aplicar_validador con distintos validadores.
    """
    lista_emails = ["test@example.com", "hola", "usuario@correo.com", "no_valido"]
    lista_numeros = [5, 12, 7, 20, 3]

    emails_validos = aplicar_validador(lista_emails, es_email_valido)
    numeros_validos = aplicar_validador(lista_numeros, es_mayor_a_10)

    print("Emails válidos:", emails_validos)
    print("Números mayores a 10:", numeros_validos)


if __name__ == "__main__":
    main()
