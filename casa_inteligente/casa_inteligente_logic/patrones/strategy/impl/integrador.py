"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\patrones\strategy\impl
Fecha: 2025-11-04 16:23:11
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\patrones\strategy\impl\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: modo_dia_strategy.py
# Ruta: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\patrones\strategy\impl\modo_dia_strategy.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/3: modo_noche_strategy.py
# Ruta: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\patrones\strategy\impl\modo_noche_strategy.py
# ================================================================================

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


