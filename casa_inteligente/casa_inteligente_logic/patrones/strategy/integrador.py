"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\patrones\strategy
Fecha: 2025-11-04 16:23:11
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\patrones\strategy\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: modo_operacion_strategy.py
# Ruta: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\patrones\strategy\modo_operacion_strategy.py
# ================================================================================

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


