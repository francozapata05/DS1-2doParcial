"""
Entidad TermostatoInteligente.
"""

from casa_inteligente_logic.entidades.dispositivos.dispositivo_climatico import DispositivoClimatico

class TermostatoInteligente(DispositivoClimatico):
    """Entidad TermostatoInteligente - solo datos."""

    def __init__(self, nombre: str):
        super().__init__(
            nombre=nombre,
            temperatura=22.0
        )
