"""
Interfaz para la estrategia de modo de operacion.
"""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from casa_inteligente_logic.entidades.espacios.habitacion import Habitacion

class ModoOperacionStrategy(ABC):
    """Interfaz para definir algoritmos de modos de operacion."""
    @abstractmethod
    def ejecutar(self, habitacion: 'Habitacion') -> None:
        pass
