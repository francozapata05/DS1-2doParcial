"""
Servicio para gestionar multiples casas.
"""

from typing import Dict, Type
from casa_inteligente_logic.entidades.espacios.registro_propiedad import RegistroPropiedad
from casa_inteligente_logic.entidades.dispositivos.dispositivo import Dispositivo
from casa_inteligente_logic.servicios.negocio.paquete import Paquete

class CasasService:
    """Servicio para operaciones de alto nivel en multiples casas."""
    def __init__(self):
        self._casas: Dict[int, RegistroPropiedad] = {}

    def add_casa(self, registro: RegistroPropiedad) -> None:
        self._casas[registro.get_id_catastral()] = registro

    def buscar_casa(self, id_catastral: int) -> RegistroPropiedad:
        if id_catastral not in self._casas:
            raise ValueError(f"Casa con catastro {id_catastral} no encontrada.")
        return self._casas[id_catastral]

    def desactivar_dispositivos(self, id_catastral: int, tipo_dispositivo: Type[Dispositivo]) -> Paquete:
        paquete = Paquete(tipo_dispositivo)
        dispositivos_desactivados = []

        for casa in self._casas.values():
            habitacion = casa.get_habitacion()
            dispositivos_en_habitacion = habitacion.get_dispositivos()
            
            for dispositivo in dispositivos_en_habitacion:
                if isinstance(dispositivo, tipo_dispositivo):
                    dispositivos_desactivados.append(dispositivo)
            
            # Remover dispositivos desactivados de la habitacion
            dispositivos_restantes = [d for d in dispositivos_en_habitacion if d not in dispositivos_desactivados]
            setattr(habitacion, '_dispositivos', dispositivos_restantes)

        for dispositivo in dispositivos_desactivados:
            paquete.agregar_dispositivo(dispositivo)

        print(f"DESACTIVANDO {len(dispositivos_desactivados)} unidades de {tipo_dispositivo}")
        return paquete
