"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\excepciones
Fecha: 2025-11-04 16:23:11
Total de archivos integrados: 5
"""

# ================================================================================
# ARCHIVO 1/5: __init__.py
# Ruta: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\excepciones\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/5: casa_inteligente_exception.py
# Ruta: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\excepciones\casa_inteligente_exception.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/5: mensajes_exception.py
# Ruta: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\excepciones\mensajes_exception.py
# ================================================================================

"""
Centralizacion de mensajes de error para excepciones.
"""

# Operacion
USER_OPERACION_INVALIDA = "La operacion no es valida."
TECH_OPERACION_INVALIDA = "La operacion no se pudo completar."

# Persistencia
USER_PERSISTENCIA_ESCRITURA = "Error al guardar el registro."
TECH_PERSISTENCIA_ESCRITURA = "Fallo la operacion de escritura en disco."
USER_PERSISTENCIA_LECTURA = "Error al leer el registro."
TECH_PERSISTENCIA_LECTURA = "Fallo la operacion de lectura de disco."
USER_PERSISTENCIA_NO_ENCONTRADO = "El registro solicitado no existe."
TECH_PERSISTENCIA_NO_ENCONTRADO = "El archivo no fue encontrado en el directorio de datos."


# ================================================================================
# ARCHIVO 4/5: operacion_invalida_exception.py
# Ruta: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\excepciones\operacion_invalida_exception.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 5/5: persistencia_exception.py
# Ruta: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\excepciones\persistencia_exception.py
# ================================================================================

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


