"""
Excepcion para cuando una operacion no es valida.
"""

from casa_inteligente_logic.excepciones.casa_inteligente_exception import CasaInteligenteException
from casa_inteligente_logic.excepciones.mensajes_exception import (
    USER_OPERACION_INVALIDA,
    TECH_OPERACION_INVALIDA
)

class OperacionInvalidaException(CasaInteligenteException):
    """Lanzada cuando una operacion no es valida."""
    def __init__(self, message: str):
        super().__init__(
            USER_OPERACION_INVALIDA,
            f"{TECH_OPERACION_INVALIDA}: {message}"
        )
