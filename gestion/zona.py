from typing import List
from gestion.zoologico import Zoologico
from zooAnimales.animal import Animal

class Zona:
    def __init__(self, nombre: str = None, zoo: Zoologico = None):
        self.nombre = nombre
        self.zoo = zoo
        self.animales: List[Animal] = []

    def agregarAnimales(self, animal: Animal):
        self.animales.append(animal)

    def cantidadAnimales(self) -> int:
        return len(self.animales)

    def getZoo(self) -> Zoologico:
        return self.zoo

    def getNombre(self) -> str:
        return self.nombre