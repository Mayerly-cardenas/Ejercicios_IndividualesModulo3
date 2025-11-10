from src.bloque_1.ejercicio_2 import crear_perfil


def test_crear_perfil_completo():
    resultado = crear_perfil(
        "Mayerly Cárdenas",
        22,
        "Leer", "Programar", "Cocinar",
        twitter="@mayarly_c",
        instagram="@mayerlyc"
    )

    assert "Mayerly Cárdenas" in resultado
    assert "22 años" in resultado
    assert "Leer, Programar, Cocinar" in resultado
    assert "Twitter: @mayarly_c" in resultado
    assert "Instagram: @mayerlyc" in resultado


def test_crear_perfil_sin_hobbies():
    resultado = crear_perfil("Juan Pérez", 30, twitter="@juanperez")
    assert "Hobbies: No especificados" in resultado
    assert "Twitter: @juanperez" in resultado


def test_crear_perfil_sin_redes():
    resultado = crear_perfil("Laura Gómez", 25, "Bailar", "Pintar")
    assert "Hobbies: Bailar, Pintar" in resultado
    assert "Redes Sociales: No registradas" in resultado
