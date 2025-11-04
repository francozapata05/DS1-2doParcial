"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\servicios\negocio
Fecha: 2025-11-04 16:23:11
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\servicios\negocio\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: casas_service.py
# Ruta: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\servicios\negocio\casas_service.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/3: paquete.py
# Ruta: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\servicios\negocio\paquete.py
# ================================================================================

"""
Clase generica para empaquetar dispositivos.
"""

from typing import Generic, TypeVar, List

T = TypeVar('T')

class Paquete(Generic[T]):
    """Caja generica para empaquetar un tipo de dispositivo."""
    _id_counter = 0

    def __init__(self, tipo_dispositivo: type):
        Paquete._id_counter += 1
        self._id_paquete = Paquete._id_counter
        self._tipo_dispositivo = tipo_dispositivo
        self._contenido: List[T] = []

    def agregar_dispositivo(self, dispositivo: T) -> None:
        if not isinstance(dispositivo, self._tipo_dispositivo):
            raise TypeError(f"Solo se pueden agregar dispositivos de tipo {self._tipo_dispositivo.__name__}")
        self._contenido.append(dispositivo)

    def get_contenido(self) -> List[T]:
        return self._contenido.copy()

    def mostrar_contenido_caja(self) -> None:
        print("Contenido de la caja:")
        print(f"  Tipo: {self._tipo_dispositivo.__name__}")
        print(f"  Cantidad: {len(self._contenido)}")
        print(f"  ID Paquete: {self._id_paquete}")


