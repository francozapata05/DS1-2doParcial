"""
Evento de sensor para el patron Observer.
"""

from datetime import datetime

class EventoSensor:
    """Representa un evento de un sensor."""
    def __init__(self, valor: float, unidad: str):
        self._valor = valor
        self._unidad = unidad
        self._timestamp = datetime.now()

    def get_valor(self) -> float:
        return self._valor

    def get_unidad(self) -> str:
        return self._unidad

    def get_timestamp(self) -> datetime:
        return self._timestamp
