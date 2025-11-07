from typing import List, Tuple

def filtrar_estudiantes_aprobados(estudiantes: List[Tuple[str, float]]) -> List[Tuple[str, float]]:
    """
    Filtra una lista de estudiantes y devuelve solo aquellos que aprobaron
    (nota >= 3.0).

    Args:
        estudiantes (List[Tuple[str, float]]): Lista de tuplas (nombre, nota).

    Returns:
        List[Tuple[str, float]]: Lista de estudiantes aprobados.
    """
    return list(filter(lambda e: e[1] >= 3.0, estudiantes))


def main():
    """
    Función principal para probar el filtrado de estudiantes aprobados.
    """
    estudiantes = [("Ana", 4.5), ("Juan", 2.8), ("Maria", 3.9), ("Pedro", 2.5)]
    aprobados = filtrar_estudiantes_aprobados(estudiantes)
    print("Estudiantes aprobados:", aprobados)


if __name__ == "__main__":
    main()
