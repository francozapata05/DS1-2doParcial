"""
Servicio para LuzInteligente.
"""

from casa_inteligente_logic.servicios.dispositivos.dispositivo_service import DispositivoService
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from casa_inteligente_logic.entidades.dispositivos.luz_inteligente import LuzInteligente

class LuzInteligenteService(DispositivoService):
    """Servicio para LuzInteligente."""

    def mostrar_datos(self, dispositivo: 'LuzInteligente') -> None:
        super().mostrar_datos(dispositivo)
        print(f"Marca: {dispositivo.get_marca()}")
        print(f"Brillo: {dispositivo.get_brillo()}% ")
