from typing import Callable

def crear_contador() -> Callable[[], int]:
    """
    Crea un contador independiente utilizando un closure.

    Returns:
        Callable[[], int]: Función que al llamarse incrementa y devuelve el conteo.
    """
    conteo = 0

    def incrementar() -> int:
        """
        Incrementa el valor del contador en 1 y lo devuelve.

        Returns:
            int: Valor actual del contador después de incrementar.
        """
        nonlocal conteo
        conteo += 1
        return conteo

    return incrementar


def main():
    """
    Función principal para probar la funcionalidad de contadores independientes.
    """
    contador1 = crear_contador()
    contador2 = crear_contador()

    print("Contador 1:")
    print(contador1())  # 1
    print(contador1())  # 2

    print("Contador 2:")
    print(contador2())  # 1
    print(contador2())  # 2
    print(contador1())  # 3


if __name__ == "__main__":
    main()
