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
