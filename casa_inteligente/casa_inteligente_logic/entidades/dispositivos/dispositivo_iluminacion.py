"""
Clase base para dispositivos de iluminacion.
"""

from casa_inteligente_logic.entidades.dispositivos.dispositivo import Dispositivo

class DispositivoIluminacion(Dispositivo):
    """Clase abstracta para dispositivos de iluminacion."""
    def __init__(self, nombre: str, brillo: int):
        super().__init__(nombre)
        self._brillo = brillo

    def get_brillo(self) -> int:
        return self._brillo

    def set_brillo(self, brillo: int) -> None:
        if not 0 <= brillo <= 100:
            raise ValueError("El brillo debe estar entre 0 y 100.")
        self._brillo = brillo
