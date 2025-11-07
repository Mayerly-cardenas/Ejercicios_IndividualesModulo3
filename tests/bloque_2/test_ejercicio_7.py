from src.bloque_2.ejercicio_7 import filtrar_estudiantes_aprobados

def test_filtrar_estudiantes_aprobados():
    estudiantes = [("Ana", 4.5), ("Juan", 2.8), ("Maria", 3.9), ("Pedro", 2.5)]
    resultado = filtrar_estudiantes_aprobados(estudiantes)
    assert resultado == [("Ana", 4.5), ("Maria", 3.9)]

def test_filtrar_todos_aprobados():
    estudiantes = [("Ana", 5.0), ("Juan", 3.5)]
    resultado = filtrar_estudiantes_aprobados(estudiantes)
    assert resultado == estudiantes

def test_filtrar_todos_reprobados():
    estudiantes = [("Ana", 2.5), ("Juan", 2.9)]
    resultado = filtrar_estudiantes_aprobados(estudiantes)
    assert resultado == []
