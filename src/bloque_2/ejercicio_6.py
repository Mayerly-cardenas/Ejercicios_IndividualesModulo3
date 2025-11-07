from typing import List, Dict

def aplicar_descuento(productos: List[Dict[str, float]], descuento: float = 0.10) -> List[float]:
    """
    Aplica un descuento a los precios de los productos y devuelve una lista
    solo con los precios descontados.

    Args:
        productos (List[Dict[str, float]]): Lista de diccionarios con productos.
        descuento (float, optional): Porcentaje de descuento a aplicar (0.10 = 10%). Defaults to 0.10.

    Returns:
        List[float]: Lista de precios con descuento aplicado.
    """
    return list(map(lambda p: round(p["precio"] * (1 - descuento), 2), productos))


def main():
    """
    Función principal para probar la aplicación de descuento a una lista de productos.
    """
    productos = [
        {"nombre": "Camisa", "precio": 50000},
        {"nombre": "Pantalón", "precio": 80000},
        {"nombre": "Zapatos", "precio": 120000},
    ]

    precios_con_descuento = aplicar_descuento(productos)
    print("Precios con descuento aplicado:", precios_con_descuento)


if __name__ == "__main__":
    main()
