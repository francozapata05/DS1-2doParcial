"""
Entidad PermisoAcceso.
"""

from datetime import date

class PermisoAcceso:
    """Certificacion de acceso de un usuario."""
    def __init__(self, permitido: bool, fecha_emision: date, observaciones: str):
        self._permitido = permitido
        self._fecha_emision = fecha_emision
        self._observaciones = observaciones

    def is_permitido(self) -> bool:
        return self._permitido

    def get_fecha_emision(self) -> date:
        return self._fecha_emision

    def get_observaciones(self) -> str:
        return self._observaciones
