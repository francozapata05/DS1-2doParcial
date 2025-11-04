"""
Servicio para Usuario.
"""

from datetime import date
from casa_inteligente_logic.entidades.usuarios.usuario import Usuario
from casa_inteligente_logic.entidades.usuarios.permiso_acceso import PermisoAcceso

class UsuarioService:
    """Servicio para operaciones de Usuario."""
    def asignar_permiso_acceso(
        self,
        usuario: Usuario,
        permitido: bool,
        fecha_emision: date,
        observaciones: str
    ) -> None:
        permiso = PermisoAcceso(permitido, fecha_emision, observaciones)
        usuario.set_permiso_acceso(permiso)

    def ejecutar_acciones(self, usuario: Usuario, fecha: date) -> bool:
        permiso = usuario.get_permiso_acceso()
        if not permiso or not permiso.is_permitido():
            print(f"El usuario {usuario.get_nombre()} no tiene permiso para ejecutar acciones.")
            return False

        acciones_del_dia = usuario.get_acciones()
        
        for accion in acciones_del_dia:
            print(f"El usuario {usuario.get_nombre()} ejecuto la accion {accion.get_id_accion()} {accion.get_descripcion()}")
        
        return True
