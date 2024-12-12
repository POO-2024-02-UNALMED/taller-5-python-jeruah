from zooAnimales.animal import Animal

class Mamifero(Animal):
    listado = []
    caballos = 0
    leones = 0

    def __init__(self, nombre: str = None, edad: int = None, habitat: str = None, genero: str = None, pelaje: bool = None, patas: int = None):
        super().__init__(nombre, edad, habitat, genero)
        self.pelaje = pelaje
        self.patas = patas
        Mamifero.listado.append(self)

    @staticmethod
    def crearCaballo(nombre: str, edad: int, genero: str) -> 'Mamifero':
        Mamifero.caballos += 1
        return Mamifero(nombre, edad, "Pradera", genero, True, 4)

    @staticmethod
    def crearLeon(nombre: str, edad: int, genero: str) -> 'Mamifero':
        Mamifero.leones += 1
        return Mamifero(nombre, edad, "selva", genero, True, 4)

    @staticmethod
    def cantidadMamiferos() -> int:
        return len(Mamifero.listado)

    def isPelaje(self) -> bool:
        return self.pelaje

    def getPatas(self) -> int:
        return self.patas