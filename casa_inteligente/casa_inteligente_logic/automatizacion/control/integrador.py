"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\automatizacion\control
Fecha: 2025-11-04 16:23:11
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\automatizacion\control\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: control_automatizacion_task.py
# Ruta: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\automatizacion\control\control_automatizacion_task.py
# ================================================================================

"""
Controlador de automatizacion.
"""

import threading
import time
from casa_inteligente_logic.patrones.observer.observer import Observer
from casa_inteligente_logic.automatizacion.sensores.temperatura_sensor_task import TemperaturaSensorTask
from casa_inteligente_logic.automatizacion.sensores.movimiento_sensor_task import MovimientoSensorTask
from casa_inteligente_logic.entidades.espacios.habitacion import Habitacion
from casa_inteligente_logic.servicios.espacios.habitacion_service import HabitacionService
from casa_inteligente_logic.entidades.dispositivos.termostato_inteligente import TermostatoInteligente

INTERVALO_CONTROL_AUTOMATIZACION = 2.5  # segundos
TEMP_MIN_TERMOSTATO = 20  # °C

class ControlAutomatizacionTask(threading.Thread, Observer):
    """Controla la automatizacion basado en sensores."""
    def __init__(
        self,
        sensor_temperatura: TemperaturaSensorTask,
        sensor_movimiento: MovimientoSensorTask,
        habitacion: Habitacion,
        habitacion_service: HabitacionService
    ):
        threading.Thread.__init__(self, daemon=True)
        self._sensor_temperatura = sensor_temperatura
        self._sensor_movimiento = sensor_movimiento
        self._habitacion = habitacion
        self._habitacion_service = habitacion_service
        self._ultima_temperatura: float = 25.0
        self._ultimo_movimiento: bool = False
        self._detenido = threading.Event()

        # Suscribirse a los sensores
        self._sensor_temperatura.agregar_observador(self)
        self._sensor_movimiento.agregar_observador(self)

    def actualizar(self, evento, sender) -> None:
        if isinstance(sender, TemperaturaSensorTask):
            self._ultima_temperatura = evento
        elif isinstance(sender, MovimientoSensorTask):
            self._ultimo_movimiento = evento

    def run(self):
        while not self._detenido.is_set():
            self._evaluar_y_actuar()
            time.sleep(INTERVALO_CONTROL_AUTOMATIZACION)

    def _evaluar_y_actuar(self):
        temp = self._ultima_temperatura
        movimiento = self._ultimo_movimiento

        print(f"[CONTROL] Temp: {temp}°C, Movimiento: {movimiento}")

        if temp < TEMP_MIN_TERMOSTATO:
            print("[CONTROL] Temperatura baja. Encendiendo termostato...")
            for dispositivo in self._habitacion.get_dispositivos():
                if isinstance(dispositivo, TermostatoInteligente):
                    dispositivo.encender()
                    print(f"[CONTROL] Termostato {dispositivo.get_nombre()} encendido.")
        
        if movimiento:
            print("[CONTROL] Movimiento detectado.")

    def detener(self) -> None:
        self._detenido.set()


