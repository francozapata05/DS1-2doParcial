"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\patrones\observer
Fecha: 2025-11-04 16:23:11
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\patrones\observer\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: observable.py
# Ruta: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\patrones\observer\observable.py
# ================================================================================

"""
Clase Observable generica para el patron Observer.
"""

from typing import Generic, TypeVar, List
from abc import ABC, abstractmethod

T = TypeVar('T')

class Observer(Generic[T], ABC):
    @abstractmethod
    def actualizar(self, evento: T, sender: 'Observable') -> None:
        pass

class Observable(Generic[T], ABC):
    def __init__(self):
        self._observadores: List[Observer[T]] = []

    def agregar_observador(self, observador: Observer[T]) -> None:
        if observador not in self._observadores:
            self._observadores.append(observador)

    def notificar_observadores(self, evento: T) -> None:
        for observador in self._observadores:
            observador.actualizar(evento, self)


# ================================================================================
# ARCHIVO 3/3: observer.py
# Ruta: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\patrones\observer\observer.py
# ================================================================================

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


