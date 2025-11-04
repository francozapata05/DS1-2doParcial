"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\automatizacion\sensores
Fecha: 2025-11-04 16:23:11
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\automatizacion\sensores\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: movimiento_sensor_task.py
# Ruta: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\automatizacion\sensores\movimiento_sensor_task.py
# ================================================================================

"""
Sensor de movimiento en tiempo real.
"""

import threading
import time
import random
from casa_inteligente_logic.patrones.observer.observable import Observable

INTERVALO_SENSOR_MOVIMIENTO = 1.0  # segundos

class MovimientoSensorTask(threading.Thread, Observable[bool]):
    """Detecta movimiento y notifica a los observadores."""
    def __init__(self):
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)
        self._detenido = threading.Event()

    def _detectar_movimiento(self) -> bool:
        return random.choice([True, False])

    def run(self):
        while not self._detenido.is_set():
            movimiento = self._detectar_movimiento()
            if movimiento:
                self.notificar_observadores(movimiento)
            time.sleep(INTERVALO_SENSOR_MOVIMIENTO)

    def detener(self) -> None:
        self._detenido.set()


# ================================================================================
# ARCHIVO 3/3: temperatura_sensor_task.py
# Ruta: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\automatizacion\sensores\temperatura_sensor_task.py
# ================================================================================

"""
Sensor de temperatura en tiempo real.
"""

import threading
import time
import random
from casa_inteligente_logic.patrones.observer.observable import Observable

INTERVALO_SENSOR_TEMPERATURA = 2.0  # segundos
SENSOR_TEMP_MIN = 15  # °C
SENSOR_TEMP_MAX = 30  # °C

class TemperaturaSensorTask(threading.Thread, Observable[float]):
    """Lee la temperatura ambiental y notifica a los observadores."""
    def __init__(self):
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)
        self._detenido = threading.Event()

    def _leer_temperatura(self) -> float:
        return round(random.uniform(SENSOR_TEMP_MIN, SENSOR_TEMP_MAX), 2)

    def run(self):
        while not self._detenido.is_set():
            temperatura = self._leer_temperatura()
            self.notificar_observadores(temperatura)
            time.sleep(INTERVALO_SENSOR_TEMPERATURA)

    def detener(self) -> None:
        self._detenido.set()


