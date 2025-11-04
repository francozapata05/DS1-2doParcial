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
