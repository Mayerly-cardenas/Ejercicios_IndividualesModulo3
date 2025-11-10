"""
Ejercicio 7: Filtrado de Estudiantes con filter

Este programa permite ingresar estudiantes con sus notas y filtra aquellos que aprobaron
(Nota >= 3.0) usando una función lambda y filter().

Conceptos aplicados:
- Funciones lambda
- filter()
- Trabajo con tuplas
- Interacción con el usuario
"""

from typing import List, Tuple


def filtrar_aprobados(estudiantes: List[Tuple[str, float]]) -> List[Tuple[str, float]]:
    """
    Filtra los estudiantes que aprobaron con nota mayor o igual a 3.0.

    Args:
        estudiantes (List[Tuple[str, float]]): Lista de tuplas (nombre, nota).

    Returns:
        List[Tuple[str, float]]: Lista de estudiantes aprobados.
    """
    return list(filter(lambda est: est[1] >= 3.0, estudiantes))


def menu_filtrar_estudiantes() -> None:
    """Muestra un menú interactivo para agregar estudiantes y filtrar aprobados."""
    estudiantes: List[Tuple[str, float]] = []

    while True:
        print("\n MENÚ FILTRO DE ESTUDIANTES ")
        print("1. Agregar estudiante")
        print("2. Ver lista completa")
        print("3. Filtrar aprobados")
        print("4. Salir al menú principal")

        opcion = input(" Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre del estudiante: ").capitalize()
            try:
                nota = float(input("Nota del estudiante (0.0 - 5.0): "))
                if 0.0 <= nota <= 5.0:
                    estudiantes.append((nombre, nota))
                    print(f" Estudiante '{nombre}' agregado correctamente.")
                else:
                    print(" La nota debe estar entre 0.0 y 5.0.")
            except ValueError:
                print(" Error: debes ingresar un número válido para la nota.")

        elif opcion == "2":
            if estudiantes:
                print("\n Lista de estudiantes:")
                for est in estudiantes:
                    print(f"- {est[0]} ({est[1]})")
            else:
                print("️ No hay estudiantes registrados.")

        elif opcion == "3":
            if estudiantes:
                aprobados = filtrar_aprobados(estudiantes)
                print("\n Estudiantes aprobados:")
                if aprobados:
                    for est in aprobados:
                        print(f"- {est[0]} ({est[1]})")
                else:
                    print("Ningún estudiante aprobó.")
            else:
                print("️ Primero agrega estudiantes antes de filtrar.")

        elif opcion == "4":
            print(" Volviendo al menú principal...")
            break
        else:
            print(" Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    menu_filtrar_estudiantes()
