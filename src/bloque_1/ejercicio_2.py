def crear_perfil(nombre: str, edad: int, *hobbies: str, **redes_sociales: str) -> str:
    """
    Genera un perfil de usuario con información básica, hobbies y redes sociales.

    Parámetros:
        nombre (str): Nombre del usuario.
        edad (int): Edad del usuario.
        *hobbies (str): Lista variable de hobbies.
        **redes_sociales (str): Diccionario con redes sociales (clave=red, valor=usuario).

    Retorna:
        str: Un string formateado con toda la información del perfil.
    """
    perfil = f" PERFIL DE USUARIO\n"
    perfil += f"Nombre: {nombre}\n"
    perfil += f"Edad: {edad} años\n"

    if hobbies:
        perfil += f"Hobbies: {', '.join(hobbies)}\n"
    else:
        perfil += "Hobbies: No especificados\n"

    if redes_sociales:
        perfil += "Redes Sociales:\n"
        for red, usuario in redes_sociales.items():
            perfil += f"  - {red.capitalize()}: {usuario}\n"
    else:
        perfil += "Redes Sociales: No registradas\n"

    return perfil

def main():
    perfil = crear_perfil(
        "Mayerly Cárdenas",
        22,
        "Leer", "Programar", "Cocinar",
        twitter="@mayarly_c",
        instagram="@mayerlyc"
    )
    print(perfil)


if __name__ == "__main__":
    main()
