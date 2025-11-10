# Ejercicio 6: Procesamiento de Datos con map y lambda

def tienda_ropa():
    productos = [
        {"nombre": "Camisa", "precio": 50000},
        {"nombre": "Pantalón", "precio": 80000},
        {"nombre": "Chaqueta", "precio": 120000},
        {"nombre": "Zapatos", "precio": 150000},
        {"nombre": "Gorra", "precio": 30000}
    ]

    while True:
        print("\n===== TIENDA DE ROPA MAYERLY =====")
        print("1. Ver productos")
        print("2. Aplicar descuento del 10%")
        print("3. Eliminar un producto")
        print("4. Realizar una compra")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n--- Lista de productos ---")
            for p in productos:
                print(f"{p['nombre']}: ${p['precio']:,}")

        elif opcion == "2":
            print("\nAplicando descuento del 10% a todos los productos...")
            productos_con_descuento = list(map(lambda p: {"nombre": p["nombre"], "precio": round(p["precio"] * 0.9, 2)}, productos))
            print("\n--- Productos con descuento ---")
            for p in productos_con_descuento:
                print(f"{p['nombre']}: ${p['precio']:,}")
            productos = productos_con_descuento  # Actualiza los precios con descuento

        elif opcion == "3":
            print("\n--- Eliminar producto ---")
            nombre = input("Ingrese el nombre del producto que desea eliminar: ").capitalize()
            productos_filtrados = list(filter(lambda p: p["nombre"] != nombre, productos))
            if len(productos_filtrados) < len(productos):
                productos = productos_filtrados
                print(f" Producto '{nombre}' eliminado exitosamente.")
            else:
                print(f" No se encontró el producto '{nombre}'.")

        elif opcion == "4":
            print("\n--- Realizar compra ---")
            carrito = []
            while True:
                nombre = input("Ingrese el nombre del producto que desea comprar (o 'fin' para terminar): ").capitalize()
                if nombre == "Fin":
                    break
                producto = next((p for p in productos if p["nombre"] == nombre), None)
                if producto:
                    carrito.append(producto)
                    print(f"'{nombre}' agregado al carrito.")
                else:
                    print(" Producto no encontrado.")

            if carrito:
                total = sum(p["precio"] for p in carrito)
                print("\n--- Resumen de compra ---")
                for p in carrito:
                    print(f"{p['nombre']}: ${p['precio']:,}")
                print(f"\n Total a pagar: ${total:,}")
            else:
                print("No se agregó ningún producto al carrito.")

        elif opcion == "5":
            print("Saliendo de la tienda... ¡Gracias por su visita! ")
            break

        else:
            print(" Opción no válida. Intente nuevamente.")


# Ejecutar la función principal
if __name__ == "__main__":
    tienda_ropa()
