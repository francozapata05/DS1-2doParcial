"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\entidades\espacios
Fecha: 2025-11-04 16:23:11
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\entidades\espacios\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/4: casa.py
# Ruta: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\entidades\espacios\casa.py
# ================================================================================

"""
Entidad Casa.
"""

class Casa:
    """Representa una casa."""
    def __init__(self, id_catastral: int, domicilio: str):
        if id_catastral <= 0:
            raise ValueError("El ID catastral debe ser mayor a cero.")
        self._id_catastral = id_catastral
        self._domicilio = domicilio

    def get_id_catastral(self) -> int:
        return self._id_catastral

    def get_domicilio(self) -> str:
        return self._domicilio

    def set_domicilio(self, domicilio: str) -> None:
        self._domicilio = domicilio


# ================================================================================
# ARCHIVO 3/4: habitacion.py
# Ruta: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\entidades\espacios\habitacion.py
# ================================================================================

"""
Entidad Habitacion.
"""

from typing import List
from casa_inteligente_logic.entidades.dispositivos.dispositivo import Dispositivo
from casa_inteligente_logic.entidades.usuarios.usuario import Usuario

class Habitacion:
    """Representa una habitacion en la casa."""
    def __init__(self, nombre: str):
        self._nombre = nombre
        self._dispositivos: List[Dispositivo] = []
        self._usuarios: List[Usuario] = []

    def get_nombre(self) -> str:
        return self._nombre

    def get_dispositivos(self) -> List[Dispositivo]:
        return self._dispositivos.copy()

    def add_dispositivo(self, dispositivo: Dispositivo) -> None:
        self._dispositivos.append(dispositivo)

    def get_usuarios(self) -> List[Usuario]:
        return self._usuarios.copy()

    def set_usuarios(self, usuarios: List[Usuario]) -> None:
        self._usuarios = usuarios


# ================================================================================
# ARCHIVO 4/4: registro_propiedad.py
# Ruta: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\entidades\espacios\registro_propiedad.py
# ================================================================================

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


