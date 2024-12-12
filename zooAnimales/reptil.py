from zooAnimales.animal import Animal

class Reptil(Animal):
    listado = []
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre: str = None, edad: int = None, habitat: str = None, genero: str = None, color_escamas: str = None, largo_cola: int = None):
        super().__init__(nombre, edad, habitat, genero)
        self.color_escamas = color_escamas
        self.largo_cola = largo_cola
        Reptil.listado.append(self)

    @staticmethod
    def crearIguana(nombre: str, edad: int, genero: str) -> 'Reptil':
        Reptil.iguanas += 1
        return Reptil(nombre, edad, "humedal", genero, "Verde", 3)

    @staticmethod
    def crearSerpiente(nombre: str, edad: int, genero: str) -> 'Reptil':
        Reptil.serpientes += 1
        return Reptil(nombre, edad, "jungla", genero, "blanco", 1)

    @staticmethod
    def cantidadReptiles() -> int:
        return len(Reptil.listado)

    def movimiento(self) -> str:
        return "reptar"

    def getColorEscamas(self) -> str:
        return self.color_escamas

    def getLargoCola(self) -> int:
        return self.largo_cola