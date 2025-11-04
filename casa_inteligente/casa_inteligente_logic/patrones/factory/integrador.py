"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\patrones\factory
Fecha: 2025-11-04 16:23:11
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\patrones\factory\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: dispositivo_factory.py
# Ruta: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\patrones\factory\dispositivo_factory.py
# ================================================================================

"""
Factory para la creacion de dispositivos.
"""

from casa_inteligente_logic.entidades.dispositivos.dispositivo import Dispositivo
from casa_inteligente_logic.entidades.dispositivos.luz_inteligente import LuzInteligente
from casa_inteligente_logic.entidades.dispositivos.termostato_inteligente import TermostatoInteligente

class DispositivoFactory:
    """Fabrica de dispositivos que encapsula la logica de creacion."""
    @staticmethod
    def crear_dispositivo(tipo: str, nombre: str) -> Dispositivo:
        factories = {
            "LuzInteligente": lambda: LuzInteligente(nombre, "Philips Hue"),
            "TermostatoInteligente": lambda: TermostatoInteligente(nombre)
        }

        if tipo not in factories:
            raise ValueError(f"Tipo de dispositivo desconocido: {tipo}")

        return factories[tipo]()


