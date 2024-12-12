from zooAnimales.animal import Animal

class Pez(Animal):
    listado = []
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre: str = None, edad: int = None, habitat: str = None, genero: str = None, color_escamas: str = None, cantidad_aletas: int = None):
        super().__init__(nombre, edad, habitat, genero)
        self.color_escamas = color_escamas
        self.cantidad_aletas = cantidad_aletas
        Pez.listado.append(self)

    @staticmethod
    def crearSalmon(nombre: str, edad: int, genero: str) -> 'Pez':
        Pez.salmones += 1
        return Pez(nombre, edad, "oceano", genero, "rojo", 6)

    @staticmethod
    def crearBacalao(nombre: str, edad: int, genero: str) -> 'Pez':
        Pez.bacalaos += 1
        return Pez(nombre, edad, "oceano", genero, "gris", 6)

    @staticmethod
    def cantidadPeces() -> int:
        return len(Pez.listado)

    def movimiento(self) -> str:
        return "nadar"

    def getColorEscamas(self) -> str:
        return self.color_escamas

    def getCantidadAletas(self) -> int:
        return self.cantidad_aletas