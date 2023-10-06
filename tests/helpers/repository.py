from autorg.domain.protocols.repository import Repository
from autorg.domain.entities.input import Input


class InMemoryRepository(Repository):
    """Esta clase al derivar de la interfaz Repository
    esta obligada a implementar todos los metodos de dicha clase.
    La idea de esta clase es reimplementar los metodos de acceso
    para almacenar los inputs (la capa de datos) para que funcionen
    directamente en memoria y nos sirva para poder ejecutar nuestras pruebas
    unitarias sin la necesidad de tener que acceder realmente al dispositivo de almacenamiento real.
    Este es un patron de diseño que se conoce como: `circuit breaker`.
    """

    def __init__(self):
        self.items: list[Input] = []

    def getAll(self) -> list[Input]:
        return self.items

    def store(self, inp: Input) -> None:
        self.items.append(inp)
