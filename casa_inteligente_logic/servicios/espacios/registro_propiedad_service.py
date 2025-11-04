"""
Servicio para RegistroPropiedad.
"""

import os
import pickle
from casa_inteligente_logic.entidades.espacios.registro_propiedad import RegistroPropiedad
from casa_inteligente_logic.servicios.dispositivos.dispositivo_service_registry import DispositivoServiceRegistry
from casa_inteligente_logic.excepciones.persistencia_exception import PersistenciaException, TipoOperacion
from casa_inteligente_logic.excepciones.mensajes_exception import (
    USER_PERSISTENCIA_ESCRITURA,
    TECH_PERSISTENCIA_ESCRITURA,
    USER_PERSISTENCIA_LECTURA,
    TECH_PERSISTENCIA_LECTURA,
    USER_PERSISTENCIA_NO_ENCONTRADO,
    TECH_PERSISTENCIA_NO_ENCONTRADO
)

DIRECTORIO_DATA = "data"
EXTENSION_DATA = ".dat"

class RegistroPropiedadService:
    """Servicio para persistencia y visualizacion de RegistroPropiedad."""
    def __init__(self):
        self._dispositivo_service_registry = DispositivoServiceRegistry.get_instance()

    def mostrar_datos(self, registro: RegistroPropiedad) -> None:
        print("REGISTRO DE PROPIEDAD")
        print("=================")
        print(f"Catastro:    {registro.get_id_catastral()}")
        print(f"Propietario: {registro.get_propietario()}")
        print(f"Avaluo:      {registro.get_avaluo()}")
        print(f"Domicilio:   {registro.get_casa().get_domicilio()}")
        print(f"Cantidad de dispositivos: {len(registro.get_habitacion().get_dispositivos())}")
        print("Listado de Dispositivos instalados")
        print("____________________________")
        for dispositivo in registro.get_habitacion().get_dispositivos():
            self._dispositivo_service_registry.mostrar_datos(dispositivo)
            print()

    def persistir(self, registro: RegistroPropiedad) -> None:
        if not os.path.exists(DIRECTORIO_DATA):
            os.makedirs(DIRECTORIO_DATA)

        nombre_archivo = os.path.join(DIRECTORIO_DATA, f"{registro.get_propietario()}{EXTENSION_DATA}")

        try:
            with open(nombre_archivo, 'wb') as f:
                pickle.dump(registro, f)
            print(f"Registro de {registro.get_propietario()} persistido exitosamente en {nombre_archivo}")
        except IOError as e:
            raise PersistenciaException(
                USER_PERSISTENCIA_ESCRITURA,
                f"{TECH_PERSISTENCIA_ESCRITURA}: {e}",
                nombre_archivo,
                TipoOperacion.ESCRITURA
            )

    @staticmethod
    def leer_registro(propietario: str) -> RegistroPropiedad:
        if not propietario:
            raise ValueError("El nombre del propietario no puede ser nulo o vacio")

        nombre_archivo = os.path.join(DIRECTORIO_DATA, f"{propietario}{EXTENSION_DATA}")

        if not os.path.exists(nombre_archivo):
            raise PersistenciaException(
                USER_PERSISTENCIA_NO_ENCONTRADO,
                TECH_PERSISTENCIA_NO_ENCONTRADO,
                nombre_archivo,
                TipoOperacion.LECTURA
            )

        try:
            with open(nombre_archivo, 'rb') as f:
                registro = pickle.load(f)
                print(f"Registro de {propietario} recuperado exitosamente desde {nombre_archivo}")
                return registro
        except (IOError, pickle.UnpicklingError) as e:
            raise PersistenciaException(
                USER_PERSISTENCIA_LECTURA,
                f"{TECH_PERSISTENCIA_LECTURA}: {e}",
                nombre_archivo,
                TipoOperacion.LECTURA
            )
