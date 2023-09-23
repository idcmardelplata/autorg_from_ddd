from autorg.domain.aggregates.collect import Collect
from autorg.domain.protocols.protocols import Repository

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

    def getAll(self) -> list[str]:
        return self.items

    def store(self, input_text: str) -> None:
        self.items.append(input_text)

    def find(self, input_text) -> bool:
        return input_text in self.items



def test_added_input_should_store_in_list():
    sut = Collect(InMemoryRepository())
    sut.input("some random input")
    assert len(sut.getAll() ) == 1

def test_added_input_should_be_unique():
    sut = Collect(InMemoryRepository())
    sut.input("some random input")
    sut.input("some random input")
    assert len(sut.getAll() ) == 1

def test_should_return_list_of_str():
    sut = Collect(InMemoryRepository())
    sut.input("some random input")
    sut.input("some random input")
    assert type (sut.getAll()) is list

def test_collect_can_hold_many_inputs():
    sut = Collect(InMemoryRepository())
    sut.input("some random input")
    sut.input("some random input 2")
    assert len(sut.getAll() ) == 2

def test_input_list_should_be_stored():
    sut = Collect(InMemoryRepository())
    sut.input("some random input")
    assert sut.getAll()[0] == "some random input"
