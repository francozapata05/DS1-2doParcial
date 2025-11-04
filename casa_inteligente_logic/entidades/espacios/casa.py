"""
Entidad Casa.
"""

class Casa:
    """Representa una casa."""
    def __init__(self, id_catastral: int, domicilio: str):
        if id_catastral <= 0:
            raise ValueError("El ID catastral debe ser mayor a cero.")
        self._id_catastral = id_catastral
        self._domicilio = domicilio

    def get_id_catastral(self) -> int:
        return self._id_catastral

    def get_domicilio(self) -> str:
        return self._domicilio

    def set_domicilio(self, domicilio: str) -> None:
        self._domicilio = domicilio
