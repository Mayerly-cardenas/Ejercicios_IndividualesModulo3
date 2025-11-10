from bloque_2.ejercicio_7 import filtrar_aprobados


def test_filtrar_aprobados_basico():
    estudiantes = [("Ana", 4.5), ("Juan", 2.8), ("Maria", 3.9)]
    resultado = filtrar_aprobados(estudiantes)
    assert resultado == [("Ana", 4.5), ("Maria", 3.9)]


def test_filtrar_aprobados_todos_aprueban():
    estudiantes = [("Luis", 3.0), ("Carla", 5.0)]
    resultado = filtrar_aprobados(estudiantes)
    assert len(resultado) == 2


def test_filtrar_aprobados_ninguno_aprueba():
    estudiantes = [("Pedro", 2.5), ("Laura", 1.8)]
    resultado = filtrar_aprobados(estudiantes)
    assert resultado == []
