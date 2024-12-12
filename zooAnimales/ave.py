from zooAnimales.animal import Animal

class Ave(Animal):
    listado = []
    halcones = 0
    aguilas = 0

    def __init__(self, nombre: str = None, edad: int = None, habitat: str = None, genero: str = None, color_plumas: str = None):
        super().__init__(nombre, edad, habitat, genero)
        self.color_plumas = color_plumas
        Ave.listado.append(self)

    @staticmethod
    def crearHalcon(nombre: str, edad: int, genero: str) -> 'Ave':
        Ave.halcones += 1
        return Ave(nombre, edad, "montañas", genero, "cafe glorioso")

    @staticmethod
    def crearAguila(nombre: str, edad: int, genero: str) -> 'Ave':
        Ave.aguilas += 1
        return Ave(nombre, edad, "montañas", genero, "blanco y amarillo")

    @staticmethod
    def cantidadAves() -> int:
        return len(Ave.listado)

    def movimiento(self) -> str:
        return "volar"

    def getColorPlumas(self) -> str:
        return self.color_plumas