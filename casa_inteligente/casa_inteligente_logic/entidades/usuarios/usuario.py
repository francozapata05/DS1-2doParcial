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
