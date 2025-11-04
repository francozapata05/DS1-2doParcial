"""
Entidad Accion.
"""

from datetime import date

class Accion:
    """Accion permitida a un usuario."""
    def __init__(self, id_accion: int, descripcion: str):
        self._id_accion = id_accion
        self._descripcion = descripcion

    def get_id_accion(self) -> int:
        return self._id_accion

    def get_descripcion(self) -> str:
        return self._descripcion
