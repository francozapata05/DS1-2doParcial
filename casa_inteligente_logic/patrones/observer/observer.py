"""
Interfaz Observer generica para el patron Observer.
"""

from typing import Generic, TypeVar, TYPE_CHECKING

if TYPE_CHECKING:
    from casa_inteligente_logic.patrones.observer.observable import Observable
from abc import ABC, abstractmethod

T = TypeVar('T')

class Observer(Generic[T], ABC):
    """Interfaz para que un objeto sea notificable de cambios."""
    @abstractmethod
    def actualizar(self, evento: T, sender: 'Observable') -> None:
        """
        Recibe una actualizacion de un objeto observable.

        Args:
            evento: El evento que se ha producido.
        """
        pass
