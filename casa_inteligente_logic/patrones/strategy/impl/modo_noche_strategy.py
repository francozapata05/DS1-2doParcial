"""
Estrategia para el modo noche.
"""

from casa_inteligente_logic.patrones.strategy.modo_operacion_strategy import ModoOperacionStrategy
from casa_inteligente_logic.entidades.dispositivos.luz_inteligente import LuzInteligente
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from casa_inteligente_logic.entidades.espacios.habitacion import Habitacion

class ModoNocheStrategy(ModoOperacionStrategy):
    """Apaga todas las luces."""
    def ejecutar(self, habitacion: 'Habitacion') -> None:
        print("Activando modo noche...")
        for dispositivo in habitacion.get_dispositivos():
            if isinstance(dispositivo, LuzInteligente):
                dispositivo.apagar()
                print(f"Apagando {dispositivo.get_nombre()}")
