import json
from typing import List, Dict
from rich.console import Console
from rich.table import Table
import os

console = Console()
ARCHIVO_INVENTARIO = "inventario.json"

def cargar_inventario() -> List[Dict]:
    """Carga el inventario desde el archivo JSON."""
    if not os.path.exists(ARCHIVO_INVENTARIO):
        return []
    with open(ARCHIVO_INVENTARIO, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def guardar_inventario(inventario: List[Dict]):
    """Guarda el inventario en el archivo JSON."""
    with open(ARCHIVO_INVENTARIO, "w", encoding="utf-8") as f:
        json.dump(inventario, f, indent=4, ensure_ascii=False)

def agregar_producto(nombre: str, cantidad: int, precio: float):
    """Agrega un producto al inventario."""
    inventario = cargar_inventario()
    inventario.append({"nombre": nombre, "cantidad": cantidad, "precio": precio})
    guardar_inventario(inventario)

def vender_producto(nombre: str, cantidad: int) -> bool:
    """Realiza una venta de un producto, devuelve True si se pudo vender."""
    inventario = cargar_inventario()
    for producto in inventario:
        if producto["nombre"] == nombre:
            if producto["cantidad"] >= cantidad:
                producto["cantidad"] -= cantidad
                guardar_inventario(inventario)
                return True
            return False
    return False

def mostrar_inventario():
    """Muestra el inventario en una tabla usando rich."""
    inventario = cargar_inventario()
    tabla = Table(title="Inventario")
    tabla.add_column("Nombre", justify="center")
    tabla.add_column("Cantidad", justify="center")
    tabla.add_column("Precio", justify="center")

    for producto in inventario:
        tabla.add_row(producto["nombre"], str(producto["cantidad"]), f"{producto['precio']:.2f}")

    console.print(tabla)
