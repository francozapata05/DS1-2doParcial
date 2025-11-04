"""
Entidad LuzInteligente.
"""

from casa_inteligente_logic.entidades.dispositivos.dispositivo_iluminacion import DispositivoIluminacion

class LuzInteligente(DispositivoIluminacion):
    """Entidad LuzInteligente - solo datos."""

    def __init__(self, nombre: str, marca: str):
        super().__init__(
            nombre=nombre,
            brillo=50
        )
        self._marca = marca

    def get_marca(self) -> str:
        return self._marca

    def set_marca(self, marca: str) -> None:
        self._marca = marca
