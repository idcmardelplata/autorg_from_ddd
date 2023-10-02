from autorg.domain.protocols.repository import Repository

class InMemoryRepository(Repository):
    """ Esta clase al derivar de la interfaz Repository 
        esta obligada a implementar todos los metodos de dicha clase.
        La idea de esta clase es reimplementar los metodos de acceso
        para almacenar los inputs (la capa de datos) para que funcionen
        directamente en memoria y nos sirva para poder ejecutar nuestras pruebas
        unitarias sin la necesidad de tener que acceder realmente al dispositivo de almacenamiento real.
        Este es un patron de diseño que se conoce como: `circuit breaker`.
    """
    items = []

    def __init__(self):
        self.items.clear()

    def getAll(self) -> list[str]:
        return self.items

    def store(self, input_text: str) -> None:
        self.items.append(input_text)
