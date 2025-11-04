"""
Clase base para dispositivos de climatizacion.
"""

from casa_inteligente_logic.entidades.dispositivos.dispositivo import Dispositivo

class DispositivoClimatico(Dispositivo):
    """Clase abstracta para dispositivos de climatizacion."""
    def __init__(self, nombre: str, temperatura: float):
        super().__init__(nombre)
        self._temperatura = temperatura

    def get_temperatura(self) -> float:
        return self._temperatura

    def set_temperatura(self, temperatura: float) -> None:
        self._temperatura = temperatura
