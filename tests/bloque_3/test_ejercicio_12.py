import csv
import os
import pytest
from src.bloque_3.ejercicio_12 import analizar_csv, crear_csv_si_no_existe


@pytest.fixture
def archivo_csv_temporal(tmp_path):
    """Crea un archivo CSV temporal para pruebas."""
    ruta = tmp_path / "estudiantes.csv"
    with open(ruta, mode='w', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["nombre", "edad", "calificacion"])
        escritor.writerow(["Ana", "15", "4.5"])
        escritor.writerow(["Luis", "16", "3.8"])
        escritor.writerow(["Sofía", "17", "4.9"])
    return ruta


def test_crear_csv_si_no_existe(tmp_path):
    """Verifica que el archivo CSV se crea correctamente si no existe."""
    ruta = tmp_path / "nuevo.csv"
    crear_csv_si_no_existe(ruta)
    assert os.path.exists(ruta), "El archivo CSV no se creó correctamente"


def test_analizar_csv_resultados_correctos(archivo_csv_temporal):
    """Verifica que los resultados del análisis son correctos."""
    resultados = analizar_csv(str(archivo_csv_temporal), "calificacion")
    assert isinstance(resultados, dict)
    assert round(resultados["promedio"], 2) == 4.4
    assert resultados["maximo"] == 4.9
    assert resultados["minimo"] == 3.8


def test_analizar_csv_columna_inexistente(archivo_csv_temporal, capsys):
    """Verifica que se maneje correctamente una columna inexistente."""
    analizar_csv(str(archivo_csv_temporal), "nota_final")
    salida = capsys.readouterr().out
    assert "no existe" in salida.lower()


def test_analizar_csv_archivo_inexistente(capsys):
    """Verifica que se maneje correctamente un archivo que no existe."""
    analizar_csv("archivo_inexistente.csv", "calificacion")
    salida = capsys.readouterr().out
    assert "no existe" in salida.lower()
