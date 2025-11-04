"""
Servicio para Casa.
"""

from casa_inteligente_logic.entidades.espacios.casa import Casa
from casa_inteligente_logic.entidades.espacios.habitacion import Habitacion

class CasaService:
    """Servicio para operaciones relacionadas con Casa."""
    def crear_casa_con_habitacion(
        self,
        id_catastral: int,
        domicilio: str,
        nombre_habitacion: str
    ) -> Casa:
        casa = Casa(id_catastral, domicilio)
        habitacion = Habitacion(nombre_habitacion)
        # Acoplamiento aqui, pero aceptable para este caso
        setattr(casa, '_habitacion', habitacion)
        return casa

    def get_habitacion(self, casa: Casa) -> Habitacion:
        return getattr(casa, '_habitacion')
