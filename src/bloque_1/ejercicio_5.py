# Variable global para la tasa de IVA
TASA_IVA: float = 0.19


def calcular_iva(precio_base: float) -> float:
    """
    Calcula el valor del IVA para un precio dado usando la variable global TASA_IVA.

    Args:
        precio_base (float): Precio base del producto.

    Returns:
        float: Valor del IVA aplicado al precio base.
    """
    return precio_base * TASA_IVA


def actualizar_tasa_iva(nueva_tasa: float) -> None:
    """
    Actualiza el valor de la variable global TASA_IVA.

    Args:
        nueva_tasa (float): Nueva tasa de IVA a aplicar.
    """
    global TASA_IVA
    TASA_IVA = nueva_tasa


def main():
    """
    Función principal para probar el cálculo de IVA antes y después de actualizar la tasa.
    """
    precio = float(input("Ingrese el precio base: "))

    print(f"IVA actual ({TASA_IVA * 100}%): {calcular_iva(precio):.2f}")

    nueva_tasa = float(input("Ingrese nueva tasa de IVA (por ejemplo 0.21 para 21%): "))
    actualizar_tasa_iva(nueva_tasa)

    print(f"IVA actualizado ({TASA_IVA * 100}%): {calcular_iva(precio):.2f}")


if __name__ == "__main__":
    main()
