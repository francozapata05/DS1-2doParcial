"""
Excepcion base para el sistema de casa inteligente.
"""

class CasaInteligenteException(Exception):
    """Clase base para excepciones del sistema."""
    def __init__(self, user_message: str, technical_message: str):
        super().__init__(f"{user_message} ({technical_message})")
        self._user_message = user_message
        self._technical_message = technical_message

    def get_user_message(self) -> str:
        return self._user_message

    def get_technical_message(self) -> str:
        return self._technical_message

    def get_full_message(self) -> str:
        return str(self)
