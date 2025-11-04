"""
Excepcion para errores de persistencia.
"""

from enum import Enum
from casa_inteligente_logic.excepciones.casa_inteligente_exception import CasaInteligenteException

class TipoOperacion(Enum):
    LECTURA = "lectura"
    ESCRITURA = "escritura"

class PersistenciaException(CasaInteligenteException):
    """Lanzada cuando ocurren errores de I/O en persistencia."""
    def __init__(self, user_message: str, technical_message: str, nombre_archivo: str, tipo_operacion: TipoOperacion):
        super().__init__(user_message, f"{technical_message} en archivo: {nombre_archivo}")
        self._nombre_archivo = nombre_archivo
        self._tipo_operacion = tipo_operacion

    def get_nombre_archivo(self) -> str:
        return self._nombre_archivo

    def get_tipo_operacion(self) -> TipoOperacion:
        return self._tipo_operacion
