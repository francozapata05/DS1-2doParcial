"""
Entidad Habitacion.
"""

from typing import List
from casa_inteligente_logic.entidades.dispositivos.dispositivo import Dispositivo
from casa_inteligente_logic.entidades.usuarios.usuario import Usuario

class Habitacion:
    """Representa una habitacion en la casa."""
    def __init__(self, nombre: str):
        self._nombre = nombre
        self._dispositivos: List[Dispositivo] = []
        self._usuarios: List[Usuario] = []

    def get_nombre(self) -> str:
        return self._nombre

    def get_dispositivos(self) -> List[Dispositivo]:
        return self._dispositivos.copy()

    def add_dispositivo(self, dispositivo: Dispositivo) -> None:
        self._dispositivos.append(dispositivo)

    def get_usuarios(self) -> List[Usuario]:
        return self._usuarios.copy()

    def set_usuarios(self, usuarios: List[Usuario]) -> None:
        self._usuarios = usuarios
