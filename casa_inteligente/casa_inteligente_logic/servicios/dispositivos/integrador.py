"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\servicios\dispositivos
Fecha: 2025-11-04 16:23:11
Total de archivos integrados: 5
"""

# ================================================================================
# ARCHIVO 1/5: __init__.py
# Ruta: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\servicios\dispositivos\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/5: dispositivo_service.py
# Ruta: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\servicios\dispositivos\dispositivo_service.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/5: dispositivo_service_registry.py
# Ruta: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\servicios\dispositivos\dispositivo_service_registry.py
# ================================================================================

"""
Registro de servicios de dispositivo (Singleton y Registry).
"""

from threading import Lock
from casa_inteligente_logic.entidades.dispositivos.dispositivo import Dispositivo
from casa_inteligente_logic.entidades.dispositivos.luz_inteligente import LuzInteligente
from casa_inteligente_logic.entidades.dispositivos.termostato_inteligente import TermostatoInteligente
from casa_inteligente_logic.servicios.dispositivos.luz_inteligente_service import LuzInteligenteService
from casa_inteligente_logic.servicios.dispositivos.termostato_inteligente_service import TermostatoInteligenteService

class DispositivoServiceRegistry:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._inicializar_servicios()
        return cls._instance

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls() # Llama al constructor
        return cls._instance

    def _inicializar_servicios(self):
        self._luz_service = LuzInteligenteService()
        self._termostato_service = TermostatoInteligenteService()

        self._mostrar_datos_handlers = {
            LuzInteligente: self._mostrar_datos_luz,
            TermostatoInteligente: self._mostrar_datos_termostato
        }

    def mostrar_datos(self, dispositivo: Dispositivo) -> None:
        tipo = type(dispositivo)
        if tipo not in self._mostrar_datos_handlers:
            raise ValueError(f"Tipo desconocido: {tipo}")
        self._mostrar_datos_handlers[tipo](dispositivo)

    def _mostrar_datos_luz(self, dispositivo):
        return self._luz_service.mostrar_datos(dispositivo)

    def _mostrar_datos_termostato(self, dispositivo):
        return self._termostato_service.mostrar_datos(dispositivo)

# ================================================================================
# ARCHIVO 4/5: luz_inteligente_service.py
# Ruta: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\servicios\dispositivos\luz_inteligente_service.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 5/5: termostato_inteligente_service.py
# Ruta: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\servicios\dispositivos\termostato_inteligente_service.py
# ================================================================================

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


