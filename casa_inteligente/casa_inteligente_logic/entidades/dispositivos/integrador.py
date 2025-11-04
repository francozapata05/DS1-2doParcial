"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\entidades\dispositivos
Fecha: 2025-11-04 16:23:11
Total de archivos integrados: 6
"""

# ================================================================================
# ARCHIVO 1/6: __init__.py
# Ruta: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\entidades\dispositivos\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/6: dispositivo.py
# Ruta: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\entidades\dispositivos\dispositivo.py
# ================================================================================

"""
Interfaz base para todos los dispositivos.
"""

from abc import ABC

class Dispositivo(ABC):
    """Clase abstracta que representa un dispositivo."""
    _id_counter = 0

    def __init__(self, nombre: str):
        Dispositivo._id_counter += 1
        self._id = Dispositivo._id_counter
        self._nombre = nombre
        self._encendido = False

    def get_id(self) -> int:
        return self._id

    def get_nombre(self) -> str:
        return self._nombre

    def is_encendido(self) -> bool:
        return self._encendido

    def encender(self) -> None:
        self._encendido = True

    def apagar(self) -> None:
        self._encendido = False


# ================================================================================
# ARCHIVO 3/6: dispositivo_climatico.py
# Ruta: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\entidades\dispositivos\dispositivo_climatico.py
# ================================================================================

"""
Clase base para dispositivos de climatizacion.
"""

from casa_inteligente_logic.entidades.dispositivos.dispositivo import Dispositivo

class DispositivoClimatico(Dispositivo):
    """Clase abstracta para dispositivos de climatizacion."""
    def __init__(self, nombre: str, temperatura: float):
        super().__init__(nombre)
        self._temperatura = temperatura

    def get_temperatura(self) -> float:
        return self._temperatura

    def set_temperatura(self, temperatura: float) -> None:
        self._temperatura = temperatura


# ================================================================================
# ARCHIVO 4/6: dispositivo_iluminacion.py
# Ruta: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\entidades\dispositivos\dispositivo_iluminacion.py
# ================================================================================

"""
Clase base para dispositivos de iluminacion.
"""

from casa_inteligente_logic.entidades.dispositivos.dispositivo import Dispositivo

class DispositivoIluminacion(Dispositivo):
    """Clase abstracta para dispositivos de iluminacion."""
    def __init__(self, nombre: str, brillo: int):
        super().__init__(nombre)
        self._brillo = brillo

    def get_brillo(self) -> int:
        return self._brillo

    def set_brillo(self, brillo: int) -> None:
        if not 0 <= brillo <= 100:
            raise ValueError("El brillo debe estar entre 0 y 100.")
        self._brillo = brillo


# ================================================================================
# ARCHIVO 5/6: luz_inteligente.py
# Ruta: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\entidades\dispositivos\luz_inteligente.py
# ================================================================================

"""
Entidad LuzInteligente.
"""

from casa_inteligente_logic.entidades.dispositivos.dispositivo_iluminacion import DispositivoIluminacion

class LuzInteligente(DispositivoIluminacion):
    """Entidad LuzInteligente - solo datos."""

    def __init__(self, nombre: str, marca: str):
        super().__init__(
            nombre=nombre,
            brillo=50
        )
        self._marca = marca

    def get_marca(self) -> str:
        return self._marca

    def set_marca(self, marca: str) -> None:
        self._marca = marca


# ================================================================================
# ARCHIVO 6/6: termostato_inteligente.py
# Ruta: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\entidades\dispositivos\termostato_inteligente.py
# ================================================================================

"""
Entidad TermostatoInteligente.
"""

from casa_inteligente_logic.entidades.dispositivos.dispositivo_climatico import DispositivoClimatico

class TermostatoInteligente(DispositivoClimatico):
    """Entidad TermostatoInteligente - solo datos."""

    def __init__(self, nombre: str):
        super().__init__(
            nombre=nombre,
            temperatura=22.0
        )


