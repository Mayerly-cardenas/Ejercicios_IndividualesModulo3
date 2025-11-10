import json
from rich.console import Console
from rich.table import Table
from typing import List, Dict

console = Console()

# ---------------- FUNCIONES PRINCIPALES ---------------- #

def cargar_inventario(nombre_archivo: str) -> List[Dict]:
    """Carga el inventario desde un archivo JSON. Si no existe, devuelve una lista vacía."""
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        console.print("Archivo no encontrado o vacío. Se creará uno nuevo.", style="yellow")
        return []


def guardar_inventario(nombre_archivo: str, inventario: List[Dict]):
    """Guarda el inventario en un archivo JSON."""
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(inventario, archivo, indent=4, ensure_ascii=False)


def agregar_producto(inventario: List[Dict]):
    """Agrega un nuevo producto al inventario."""
    nombre = input("Ingrese el nombre del producto: ")
    try:
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad disponible: "))
    except ValueError:
        console.print("Error: Ingrese valores numéricos válidos para precio y cantidad.", style="red")
        return

    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    inventario.append(producto)
    console.print(f"Producto '{nombre}' agregado correctamente.", style="green")


def vender_producto(inventario: List[Dict]):
    """Permite registrar una venta de un producto existente."""
    nombre = input("Ingrese el nombre del producto a vender: ")

    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            try:
                cantidad_vendida = int(input("Ingrese la cantidad vendida: "))
            except ValueError:
                console.print("Error: Ingrese un número válido.", style="red")
                return

            if cantidad_vendida <= 0:
                console.print("La cantidad debe ser positiva.", style="red")
                return
            if cantidad_vendida > producto["cantidad"]:
                console.print("No hay suficiente stock disponible.", style="yellow")
                return

            producto["cantidad"] -= cantidad_vendida
            console.print(f"Venta registrada. Quedan {producto['cantidad']} unidades de '{nombre}'.", style="green")
            return

    console.print("Producto no encontrado en el inventario.", style="red")


def mostrar_inventario(inventario: List[Dict]):
    """Muestra el inventario actual en una tabla formateada con Rich."""
    if not inventario:
        console.print("El inventario está vacío.", style="yellow")
        return

    tabla = Table(title="Inventario de Productos")
    tabla.add_column("Nombre", justify="left", style="cyan")
    tabla.add_column("Precio", justify="right", style="magenta")
    tabla.add_column("Cantidad", justify="center", style="green")

    for producto in inventario:
        tabla.add_row(producto["nombre"], f"${producto['precio']:.2f}", str(producto["cantidad"]))

    console.print(tabla)


# ---------------- FUNCIÓN PRINCIPAL ---------------- #

def main():
    nombre_archivo = "inventario.json"
    inventario = cargar_inventario(nombre_archivo)

    while True:
        console.print("\n[bold cyan]=== GESTOR DE INVENTARIO ===[/bold cyan]")
        console.print("1. Mostrar inventario")
        console.print("2. Agregar producto")
        console.print("3. Registrar venta")
        console.print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_inventario(inventario)
        elif opcion == "2":
            agregar_producto(inventario)
            guardar_inventario(nombre_archivo, inventario)
        elif opcion == "3":
            vender_producto(inventario)
            guardar_inventario(nombre_archivo, inventario)
        elif opcion == "4":
            guardar_inventario(nombre_archivo, inventario)
            console.print("Inventario guardado. Saliendo del programa...", style="yellow")
            break
        else:
            console.print("Opción inválida. Intente nuevamente.", style="red")


if __name__ == "__main__":
    main()
