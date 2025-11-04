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