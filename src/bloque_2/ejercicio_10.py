def explorar_estructura(elemento, profundidad=1):
    """
    Función recursiva que imprime los valores no-iterables de una estructura
    (listas, tuplas, diccionarios) con su profundidad.
    """
    if isinstance(elemento, dict):
        for valor in elemento.values():
            explorar_estructura(valor, profundidad + 1)
    elif isinstance(elemento, (list, tuple)):
        for item in elemento:
            explorar_estructura(item, profundidad + 1)
    else:
        print(f"Valor: {elemento}, Profundidad: {profundidad}")
