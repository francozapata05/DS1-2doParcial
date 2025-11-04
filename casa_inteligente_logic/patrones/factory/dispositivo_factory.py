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
