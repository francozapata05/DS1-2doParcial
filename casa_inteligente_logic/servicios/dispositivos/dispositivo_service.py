"""
Servicio base para todos los dispositivos.
"""

from abc import ABC
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from casa_inteligente_logic.entidades.dispositivos.dispositivo import Dispositivo

class DispositivoService(ABC):
    """Servicio abstracto para operaciones de dispositivo."""
    def mostrar_datos(self, dispositivo: 'Dispositivo') -> None:
        print(f"Dispositivo: {type(dispositivo).__name__}")
        print(f"Nombre: {dispositivo.get_nombre()}")
        print(f"Encendido: {dispositivo.is_encendido()}")
