"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\entidades\usuarios
Fecha: 2025-11-04 16:23:11
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\entidades\usuarios\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/4: accion.py
# Ruta: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\entidades\usuarios\accion.py
# ================================================================================

"""
Entidad Accion.
"""

from datetime import date

class Accion:
    """Accion permitida a un usuario."""
    def __init__(self, id_accion: int, descripcion: str):
        self._id_accion = id_accion
        self._descripcion = descripcion

    def get_id_accion(self) -> int:
        return self._id_accion

    def get_descripcion(self) -> str:
        return self._descripcion


# ================================================================================
# ARCHIVO 3/4: permiso_acceso.py
# Ruta: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\entidades\usuarios\permiso_acceso.py
# ================================================================================

"""
Entidad PermisoAcceso.
"""

from datetime import date

class PermisoAcceso:
    """Certificacion de acceso de un usuario."""
    def __init__(self, permitido: bool, fecha_emision: date, observaciones: str):
        self._permitido = permitido
        self._fecha_emision = fecha_emision
        self._observaciones = observaciones

    def is_permitido(self) -> bool:
        return self._permitido

    def get_fecha_emision(self) -> date:
        return self._fecha_emision

    def get_observaciones(self) -> str:
        return self._observaciones


# ================================================================================
# ARCHIVO 4/4: usuario.py
# Ruta: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\entidades\usuarios\usuario.py
# ================================================================================

"""
Entidad Usuario.
"""

from typing import List, Optional
from casa_inteligente_logic.entidades.usuarios.accion import Accion
from casa_inteligente_logic.entidades.usuarios.permiso_acceso import PermisoAcceso

class Usuario:
    """Representa un usuario de la casa."""
    def __init__(self, dni: int, nombre: str, acciones: List[Accion]):
        self._dni = dni
        self._nombre = nombre
        self._acciones = acciones
        self._permiso_acceso: Optional[PermisoAcceso] = None

    def get_dni(self) -> int:
        return self._dni

    def get_nombre(self) -> str:
        return self._nombre

    def get_acciones(self) -> List[Accion]:
        return self._acciones.copy()  # Defensive copy

    def get_permiso_acceso(self) -> Optional[PermisoAcceso]:
        return self._permiso_acceso

    def set_permiso_acceso(self, permiso: PermisoAcceso) -> None:
        self._permiso_acceso = permiso


