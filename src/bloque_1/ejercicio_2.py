from typing import Tuple, Dict


def crear_perfil(nombre: str, edad: int, *hobbies: str, **redes_sociales: str) -> str:
    """
    Crea un perfil de usuario formateado con nombre, edad, hobbies y redes sociales.

    Args:
        nombre (str): Nombre del usuario.
        edad (int): Edad del usuario.
        *hobbies (str): Lista de hobbies del usuario.
        **redes_sociales (str): Redes sociales donde la clave es el nombre de la red
            y el valor es el usuario.

    Returns:
        str: Perfil del usuario en formato legible.
    """
    perfil = f"Nombre: {nombre}\nEdad: {edad}\n"

    if hobbies:
        perfil += f"Hobbies: {', '.join(hobbies)}\n"
    else:
        perfil += "Hobbies: Ninguno\n"

    if redes_sociales:
        redes = ", ".join(f"{red}: {usuario}" for red, usuario in redes_sociales.items())
        perfil += f"Redes sociales: {redes}"
    else:
        perfil += "Redes sociales: Ninguna"

    return perfil


def main():
    """
    Función principal que solicita datos del usuario y muestra el perfil completo.
    """
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))

    # Pedir hobbies separados por coma
    hobbies_input = input("Ingrese sus hobbies separados por coma (opcional): ")
    hobbies = tuple(h.strip() for h in hobbies_input.split(",")) if hobbies_input else ()

    # Pedir redes sociales
    redes_input = input("Ingrese redes sociales en formato red=usuario, separadas por coma (opcional): ")
    redes_sociales: Dict[str, str] = {}
    if redes_input:
        for r in redes_input.split(","):
            if "=" in r:
                red, usuario = r.split("=", 1)
                redes_sociales[red.strip()] = usuario.strip()

    perfil = crear_perfil(nombre, edad, *hobbies, **redes_sociales)
    print("\n--- Perfil de Usuario ---")
    print(perfil)


if __name__ == "__main__":
    main()
