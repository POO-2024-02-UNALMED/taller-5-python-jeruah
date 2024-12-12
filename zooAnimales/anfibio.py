from zooAnimales.animal import Animal

class Anfibio(Animal):
    ranas = 0
    salamandras = 0
    listado = []

    def __init__(self, nombre: str = None, edad: int = None, habitat: str = None, genero: str = None, color_piel: str = None, venenoso: bool = None):
        super().__init__(nombre, edad, habitat, genero)
        self.color_piel = color_piel
        self.venenoso = venenoso
        Anfibio.listado.append(self)

    @staticmethod
    def crearRana(nombre: str, edad: int, genero: str) -> 'Anfibio':
        Anfibio.ranas += 1
        return Anfibio(nombre, edad, "selva", genero, "rojo", True)

    @staticmethod
    def crearSalamandra(nombre: str, edad: int, genero: str) -> 'Anfibio':
        Anfibio.salamandras += 1
        return Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)

    @staticmethod
    def cantidadAnfibios() -> int:
        return len(Anfibio.listado)

    def movimiento(self) -> str:
        return "saltar"

    def getColorPiel(self) -> str:
        return self.color_piel

    def isVenenoso(self) -> bool:
        return self.venenoso