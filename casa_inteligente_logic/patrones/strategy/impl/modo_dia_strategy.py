"""
Estrategia para el modo dia.
"""

from casa_inteligente_logic.patrones.strategy.modo_operacion_strategy import ModoOperacionStrategy
from casa_inteligente_logic.entidades.dispositivos.luz_inteligente import LuzInteligente
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from casa_inteligente_logic.entidades.espacios.habitacion import Habitacion

class ModoDiaStrategy(ModoOperacionStrategy):
    """Enciende todas las luces."""
    def ejecutar(self, habitacion: 'Habitacion') -> None:
        print("Activando modo dia...")
        for dispositivo in habitacion.get_dispositivos():
            if isinstance(dispositivo, LuzInteligente):
                dispositivo.encender()
                print(f"Encendiendo {dispositivo.get_nombre()}")
