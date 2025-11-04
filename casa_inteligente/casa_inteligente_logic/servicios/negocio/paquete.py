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
