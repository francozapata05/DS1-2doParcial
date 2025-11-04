"""
Entidad RegistroPropiedad.
"""

from casa_inteligente_logic.entidades.espacios.casa import Casa
from casa_inteligente_logic.entidades.espacios.habitacion import Habitacion

class RegistroPropiedad:
    """Vincula casa, habitacion, propietario y avaluo."""
    def __init__(self, id_catastral: int, casa: Casa, habitacion: Habitacion, propietario: str, avaluo: float):
        self._id_catastral = id_catastral
        self._casa = casa
        self._habitacion = habitacion
        self._propietario = propietario
        self._avaluo = avaluo

    def get_id_catastral(self) -> int:
        return self._id_catastral

    def get_casa(self) -> Casa:
        return self._casa

    def get_habitacion(self) -> Habitacion:
        return self._habitacion

    def get_propietario(self) -> str:
        return self._propietario

    def get_avaluo(self) -> float:
        return self._avaluo
