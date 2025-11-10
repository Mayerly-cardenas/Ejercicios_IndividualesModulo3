"""
Ejercicio 5: Calculadora de Impuestos con Scope Global

Simula el cálculo de impuestos donde la tasa puede cambiar.

Conceptos aplicados:
- Scope Global vs. Local
- Uso de la palabra clave 'global'
- Buenas prácticas en funciones
"""

# Variable global
TASA_IVA = 0.19


def calcular_iva(precio_base: float) -> float:
    """
    Calcula el IVA según la tasa global actual.

    Args:
        precio_base (float): Precio sin IVA.

    Returns:
        float: Valor del IVA calculado.
    """
    return precio_base * TASA_IVA


def actualizar_tasa_iva(nueva_tasa: float) -> None:
    """
    Actualiza el valor de la tasa global de IVA.

    Args:
        nueva_tasa (float): Nuevo valor para la tasa de IVA.
    """
    global TASA_IVA
    TASA_IVA = nueva_tasa


def main():
    """
    Muestra un menú interactivo para calcular IVA o actualizar la tasa.
    """
    while True:
        print("\n===== CALCULADORA DE IVA =====")
        print(f"Tasa actual de IVA: {TASA_IVA * 100:.1f}%")
        print("1. Calcular IVA")
        print("2. Actualizar tasa de IVA")
        print("3. Salir")

        opcion = input("Seleccione una opción (1-3): ")

        if opcion == "1":
            try:
                precio = float(input("Ingrese el precio base: "))
                iva = calcular_iva(precio)
                total = precio + iva
                print(f"\nPrecio base: ${precio:.2f}")
                print(f"IVA ({TASA_IVA * 100:.1f}%): ${iva:.2f}")
                print(f"Total a pagar: ${total:.2f}")
            except ValueError:
                print(" Por favor ingrese un número válido.")

        elif opcion == "2":
            try:
                nueva_tasa = float(input("Ingrese la nueva tasa de IVA (ej. 0.16 para 16%): "))
                actualizar_tasa_iva(nueva_tasa)
                print(f" Tasa actualizada a {TASA_IVA * 100:.1f}% correctamente.")
            except ValueError:
                print(" Ingrese un número válido para la tasa.")

        elif opcion == "3":
            print(" Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print(" Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()
