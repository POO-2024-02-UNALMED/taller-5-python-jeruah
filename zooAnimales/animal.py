from zooAnimales.utlis import totalPorTipoUtil

class Animal:
    total_animales = 0

    def __init__(self, nombre: str = None, edad: int = None, habitat: str = None, genero: str = None):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero
        self.zona = None
        Animal.total_animales += 1

    def movimiento(self) -> str:
        return "desplazarse"

    @staticmethod
    def totalPorTipo() -> str:
        return totalPorTipoUtil()

    def toString(self) -> str:
        if self.zona is None:
            return f"Mi nombre es {self.nombre}, tengo una edad de {self.edad}, habito en {self.habitat} y mi genero es {self.genero}"
        else:
            return f"Mi nombre es {self.nombre}, tengo una edad de {self.edad}, habito en {self.habitat} y mi genero es {self.genero}, la zona en la que me ubico es {self.zona.get_nombre()}, en el {self.zona.get_zoo().get_nombre()}."

    def getNombre(self) -> str:
        return self.nombre

    def getEdad(self) -> int:
        return self.edad

    def getHabitat(self) -> str:
        return self.habitat

    def getGenero(self) -> str:
        return self.genero