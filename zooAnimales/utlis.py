from zooAnimales.reptil import Reptil
from zooAnimales.pez import Pez
from zooAnimales.ave import Ave
from zooAnimales.mamifero import Mamifero
from zooAnimales.anfibio import Anfibio

def totalPorTipoUtil() -> str:
    total_reptiles = Reptil.cantidadReptiles()
    total_pez = Pez.cantidadPeces()
    total_aves = Ave.cantidadAves()
    total_mamiferos = Mamifero.cantidadMamiferos()
    total_anfibio = Anfibio.cantidadAnfibios()
    message = f"Mamiferos: {total_mamiferos}\nAves: {total_aves}\nReptiles: {total_reptiles}\nPeces: {total_pez}\nAnfibios: {total_anfibio}"
    return message