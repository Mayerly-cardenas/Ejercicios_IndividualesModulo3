import csv
from rich.console import Console
from rich.table import Table

console = Console()

def crear_csv_si_no_existe(nombre_archivo: str):
    """Crea el archivo CSV con encabezados si no existe."""
    try:
        with open(nombre_archivo, mode='x', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(["nombre", "edad", "calificacion"])
            console.print(f"Archivo '{nombre_archivo}' creado correctamente.", style="green")
    except FileExistsError:
        pass  # Ya existe, no se hace nada


def agregar_estudiante(nombre_archivo: str):
    """Permite ingresar estudiantes manualmente."""
    with open(nombre_archivo, mode='a', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        nombre = input("Ingrese el nombre del estudiante: ")
        edad = input("Ingrese la edad: ")
        calificacion = input("Ingrese la calificación: ")
        escritor.writerow([nombre, edad, calificacion])
        console.print("Estudiante agregado correctamente.\n", style="green")


def analizar_csv(nombre_archivo: str, columna: str) -> dict:
    """Lee el archivo CSV y calcula promedio, máximo y mínimo de la columna indicada."""
    try:
        with open(nombre_archivo, mode='r', newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            datos = list(lector)

            if columna not in lector.fieldnames:
                console.print(f"La columna '{columna}' no existe en el archivo.", style="red")
                return {}

            valores = [float(fila[columna]) for fila in datos if fila[columna].replace('.', '', 1).isdigit()]

            if not valores:
                console.print(f"No hay datos numéricos válidos en la columna '{columna}'.", style="yellow")
                return {}

            promedio = sum(valores) / len(valores)
            maximo = max(valores)
            minimo = min(valores)

            resultados = {
                "promedio": promedio,
                "maximo": maximo,
                "minimo": minimo
            }

            # Mostrar resultados en tabla
            tabla = Table(title="Análisis de Datos CSV")
            tabla.add_column("Métrica", style="cyan", justify="left")
            tabla.add_column("Valor", style="magenta", justify="right")
            for k, v in resultados.items():
                tabla.add_row(k.capitalize(), str(round(v, 2)))

            console.print(tabla)
            return resultados

    except FileNotFoundError:
        console.print(f"El archivo '{nombre_archivo}' no existe.", style="red")
        return {}


def main():
    nombre_archivo = "estudiantes.csv"
    crear_csv_si_no_existe(nombre_archivo)

    while True:
        console.print("\n[bold cyan]=== MENÚ PRINCIPAL ===[/bold cyan]")
        console.print("1. Agregar estudiante")
        console.print("2. Analizar calificaciones")
        console.print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_estudiante(nombre_archivo)
        elif opcion == "2":
            analizar_csv(nombre_archivo, "calificacion")
        elif opcion == "3":
            console.print("Saliendo del programa...", style="yellow")
            break
        else:
            console.print("Opción inválida. Intente nuevamente.", style="red")


if __name__ == "__main__":
    main()
