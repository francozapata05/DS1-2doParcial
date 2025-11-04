"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\servicios\espacios
Fecha: 2025-11-04 16:23:11
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\servicios\espacios\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/4: casa_service.py
# Ruta: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\servicios\espacios\casa_service.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/4: habitacion_service.py
# Ruta: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\servicios\espacios\habitacion_service.py
# ================================================================================

"""
Servicio para Habitacion.
"""

from casa_inteligente_logic.entidades.espacios.habitacion import Habitacion
from casa_inteligente_logic.patrones.factory.dispositivo_factory import DispositivoFactory
from casa_inteligente_logic.excepciones.operacion_invalida_exception import OperacionInvalidaException
from casa_inteligente_logic.servicios.dispositivos.dispositivo_service_registry import DispositivoServiceRegistry

class HabitacionService:
    """Servicio para operaciones de Habitacion."""
    def __init__(self):
        self._dispositivo_service_registry = DispositivoServiceRegistry.get_instance()

    def instalar_dispositivo(self, habitacion: Habitacion, tipo: str, nombre: str) -> None:
        nuevo_dispositivo = DispositivoFactory.crear_dispositivo(tipo, nombre)
        habitacion.add_dispositivo(nuevo_dispositivo)

    def activar_modo(self, habitacion: Habitacion, modo) -> None:
        modo.ejecutar(habitacion)


# ================================================================================
# ARCHIVO 4/4: registro_propiedad_service.py
# Ruta: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\servicios\espacios\registro_propiedad_service.py
# ================================================================================

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


