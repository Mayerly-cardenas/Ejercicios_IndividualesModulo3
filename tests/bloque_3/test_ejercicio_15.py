import pytest
import os
import json
from unittest.mock import patch
from typing import List, Dict, Union
import tempfile

# La importación corregida debe ser 'ejercicio_15'
from src.bloque_3.ejercicio_15 import (
    inicializar_biblioteca,
    prestar_libro,
    devolver_libro,
    buscar_libro,
    ver_libros_prestados,
    guardar_estado,
    BIBLIOTECA_FILE
)

Libro = Dict[str, Union[str, None]]

# Datos de prueba consistentes con la implementación
DATOS_MOCK: List[Libro] = [
    {"libro_id": "001", "titulo": "Cien Años de Soledad", "autor": "García Márquez", "prestado_a": None},
    {"libro_id": "002", "titulo": "1984", "autor": "George Orwell", "prestado_a": "Juan Pérez"},
    {"libro_id": "003", "titulo": "El Señor de los Anillos", "autor": "J.R.R. Tolkien", "prestado_a": None},
]


@pytest.fixture
def mock_filesystem():
    """
    Crea un entorno de sistema de archivos temporal para las pruebas de I/O.
    Parchea la ruta del archivo BIBLIOTECA_FILE para que use este entorno temporal.
    """
    temp_dir = tempfile.mkdtemp()

    # Crea el archivo de biblioteca temporal con los datos de prueba
    temp_biblioteca_path = os.path.join(temp_dir, BIBLIOTECA_FILE)
    with open(temp_biblioteca_path, 'w', encoding='utf-8') as f:
        json.dump(DATOS_MOCK, f)

    # Parchea BIBLIOTECA_FILE a nivel de módulo para apuntar al archivo temporal.
    # Se usa la ruta corregida: 'src.bloque_3.ejercicio_15'
    with patch('src.bloque_3.ejercicio_15.BIBLIOTECA_FILE', temp_biblioteca_path):
        yield temp_biblioteca_path


# --- Tests de I/O y Estado ---

def test_inicializar_biblioteca_existente(mock_filesystem: str):
    """Verifica la carga correcta de datos si el archivo JSON existe y es válido."""
    libros = inicializar_biblioteca()
    assert len(libros) == 3
    assert libros[1]['prestado_a'] == "Juan Pérez"
    assert libros[0]['titulo'] == "Cien Años de Soledad"


def test_guardar_estado_actualiza_archivo(mock_filesystem: str):
    """Verifica que guardar_estado escriba el nuevo estado en el archivo."""
    nuevos_libros = [{"libro_id": "100", "titulo": "Nuevo Libro", "prestado_a": "Tester"}]
    guardar_estado(nuevos_libros)

    # Leer directamente el archivo para verificar el contenido
    with open(mock_filesystem, 'r', encoding='utf-8') as f:
        datos_guardados = json.load(f)

    assert len(datos_guardados) == 1
    assert datos_guardados[0]['titulo'] == "Nuevo Libro"
    assert datos_guardados[0]['prestado_a'] == "Tester"


# --- Tests de Lógica de Negocio ---

def test_prestar_libro_disponible(mock_filesystem: str):
    """Prueba el préstamo de un libro disponible (ID 001)."""
    libros = inicializar_biblioteca()

    assert prestar_libro(libros, "001", "María Sol") is True
    assert libros[0]['prestado_a'] == "María Sol"

    # Verifica que el estado se haya guardado y persista
    guardar_estado(libros)  # Guardar estado explícitamente después de la operación
    guardar_libros = inicializar_biblioteca()
    assert guardar_libros[0]['prestado_a'] == "María Sol"


def test_prestar_libro_ya_prestado(mock_filesystem: str):
    """Prueba el intento de prestar un libro que ya está prestado (ID 002)."""
    libros = inicializar_biblioteca()

    assert prestar_libro(libros, "002", "Nuevo Lector") is False
    assert libros[1]['prestado_a'] == "Juan Pérez"  # Debe seguir prestado a Juan


def test_devolver_libro_prestado(mock_filesystem: str):
    """Prueba la devolución de un libro prestado (ID 002)."""
    libros = inicializar_biblioteca()

    assert devolver_libro(libros, "002") is True
    assert libros[1]['prestado_a'] is None

    # Verifica que el estado se haya guardado y persista
    guardar_estado(libros)  # Guardar estado explícitamente después de la operación
    guardar_libros = inicializar_biblioteca()
    assert guardar_libros[1]['prestado_a'] is None


def test_devolver_libro_disponible(mock_filesystem: str):
    """Prueba la devolución de un libro que ya está disponible (ID 001)."""
    libros = inicializar_biblioteca()

    # El libro 001 no está prestado en los datos iniciales
    assert libros[0]['prestado_a'] is None

    # Intentar devolverlo debería ser Falso
    assert devolver_libro(libros, "001") is False


def test_buscar_libro_por_titulo(mock_filesystem: str):
    """Prueba la función de búsqueda por título (insensible a mayúsculas)."""
    libros = inicializar_biblioteca()

    # Búsqueda parcial y en minúsculas
    resultados = buscar_libro(libros, "años")
    assert len(resultados) == 1
    assert resultados[0]['libro_id'] == "001"

    # Búsqueda por ID (debe fallar si no es por título)
    resultados = buscar_libro(libros, "002")
    assert len(resultados) == 0

    # Búsqueda que no existe
    resultados = buscar_libro(libros, "crónicas marcianas")
    assert len(resultados) == 0


def test_ver_libros_prestados(mock_filesystem: str):
    """Verifica que solo se listen los libros prestados."""
    libros = inicializar_biblioteca()

    prestados = ver_libros_prestados(libros)

    assert len(prestados) == 1
    assert prestados[0]['libro_id'] == "002"
    assert prestados[0]['prestado_a'] == "Juan Pérez"