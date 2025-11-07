from src.bloque_1.ejercicio_2 import crear_perfil


def test_crear_perfil_sin_hobbies_ni_redes():
    perfil = crear_perfil("Ana", 25)
    assert "Nombre: Ana" in perfil
    assert "Edad: 25" in perfil
    assert "Hobbies: Ninguno" in perfil
    assert "Redes sociales: Ninguna" in perfil


def test_crear_perfil_con_hobbies():
    perfil = crear_perfil("Juan", 30, "futbol", "leer")
    assert "Hobbies: futbol, leer" in perfil


def test_crear_perfil_con_redes():
    perfil = crear_perfil("María", 22, twitter="@maria", instagram="@maria_insta")
    assert "Redes sociales: twitter: @maria, instagram: @maria_insta" in perfil


def test_crear_perfil_completo():
    perfil = crear_perfil("Pedro", 28, "cine", "guitarra", facebook="@pedro_fb", linkedin="@pedro_li")
    assert "Nombre: Pedro" in perfil
    assert "Edad: 28" in perfil
    assert "Hobbies: cine, guitarra" in perfil
    assert "Redes sociales: facebook: @pedro_fb, linkedin: @pedro_li" in perfil
