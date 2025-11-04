"""
Servicio para TermostatoInteligente.
"""

from casa_inteligente_logic.servicios.dispositivos.dispositivo_service import DispositivoService
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from casa_inteligente_logic.entidades.dispositivos.termostato_inteligente import TermostatoInteligente

class TermostatoInteligenteService(DispositivoService):
    """Servicio para TermostatoInteligente."""

    def mostrar_datos(self, dispositivo: 'TermostatoInteligente') -> None:
        super().mostrar_datos(dispositivo)
        print(f"Temperatura: {dispositivo.get_temperatura()} C")
