"""
Interfaz base para todos los dispositivos.
"""

from abc import ABC

class Dispositivo(ABC):
    """Clase abstracta que representa un dispositivo."""
    _id_counter = 0

    def __init__(self, nombre: str):
        Dispositivo._id_counter += 1
        self._id = Dispositivo._id_counter
        self._nombre = nombre
        self._encendido = False

    def get_id(self) -> int:
        return self._id

    def get_nombre(self) -> str:
        return self._nombre

    def is_encendido(self) -> bool:
        return self._encendido

    def encender(self) -> None:
        self._encendido = True

    def apagar(self) -> None:
        self._encendido = False
