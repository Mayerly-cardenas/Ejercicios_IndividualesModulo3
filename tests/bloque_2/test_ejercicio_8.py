from src.bloque_2.ejercicio_8 import palabras_mayusculas_largas, longitud_palabras

def test_palabras_mayusculas_largas():
    texto = "ESTO es un EJEMPLO de TEXTO con PALABRAS MAYUSCULAS y algunas CORTAS"
    resultado = palabras_mayusculas_largas(texto)
    # Solo las palabras en mayúsculas y con más de 5 letras
    assert resultado == ["EJEMPLO", "PALABRAS", "MAYUSCULAS"]

def test_longitud_palabras():
    palabras = ["EJEMPLO", "PALABRAS", "MAYUSCULAS"]
    resultado = longitud_palabras(palabras)
    assert resultado == {"EJEMPLO": 7, "PALABRAS": 8, "MAYUSCULAS": 10}

def test_palabras_mayusculas_largas_vacia():
    texto = "esto es todo minusculas"
    assert palabras_mayusculas_largas(texto) == []

def test_longitud_palabras_vacia():
    assert longitud_palabras([]) == {}
