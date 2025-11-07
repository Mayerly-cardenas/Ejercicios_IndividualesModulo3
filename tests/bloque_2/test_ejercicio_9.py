from src.bloque_2.ejercicio_9 import suma_numeros, concatenar_strings

def test_suma_numeros():
    numeros = [1, 2, 3, 4, 5]
    assert suma_numeros(numeros) == 15

def test_suma_numeros_vacio():
    assert suma_numeros([]) == 0

def test_concatenar_strings():
    strings = ["Hola", " ", "SENA", "!"]
    assert concatenar_strings(strings) == "Hola SENA!"

def test_concatenar_strings_vacio():
    assert concatenar_strings([]) == ""
