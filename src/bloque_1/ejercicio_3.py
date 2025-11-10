def crear_contador():
    """
    Crea un contador de llamadas usando un closure (función interna que recuerda su estado).

    Returns:
        function: Una función que, al ser llamada, incrementa y devuelve el conteo actual.
    """
    conteo = 0

    def incrementar() -> int:
        """
        Incrementa el contador en 1 y devuelve su valor actualizado.

        Returns:
            int: El número de veces que se ha llamado la función.
        """
        nonlocal conteo
        conteo += 1
        return conteo

    return incrementar


def main():
    """Demostración del funcionamiento del closure."""
    contador_a = crear_contador()
    contador_b = crear_contador()

    print(" Contador A:")
    print(contador_a())  # 1
    print(contador_a())  # 2
    print(contador_a())  # 3

    print("\n Contador B:")
    print(contador_b())  # 1
    print(contador_b())  # 2


if __name__ == "__main__":
    main()
