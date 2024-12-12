from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from gestion.zona import Zona

class Zoologico:
    def __init__(self, nombre: str = None, ubicacion: str = None):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.zonas: List['Zona'] = []

    def agregarZonas(self, zona: 'Zona'):
        self.zonas.append(zona)

    def cantidadTotalAnimales(self) -> int:
        cantidad = 0
        for zona in self.zonas:
            cantidad += zona.cantidadAnimales()
        return cantidad

    def getNombre(self) -> str:
        return self.nombre

    def getZona(self) -> List['Zona']:
        return self.zonas