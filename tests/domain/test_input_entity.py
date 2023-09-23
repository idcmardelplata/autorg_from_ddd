import pytest
from datetime import datetime
from typing import Protocol


# TODO: El input deberia tener metadatos por defecto?
# TODO: ¿Que sucede si no se especifican los metadatos?
# TODO: ¿Que tipos de metadatos son estrictamente necesarios que tenga un input?
# TODO: ¿Es responsabilidad del input procesar los metadatos?
# TODO: ¿Donde vamos a almacenar temporalmente los inputs?
# TODO: ¿Es necesario un `CRUD` de inputs?
# TODO: ¿Es necesario poder buscar un input?
# TODO: ¿La bandeja de inputs debe dar todas las opciones para gestionar inputs?
# TODO: Una vez procesados el inputs y los metadatos, ¿en que formato deberia pasarle la informacion al clarificador?
# TODO: ¿Que datos necesita minimamente el clarificador para poder trabajar?
# TEST: ¿Deberia crear un helper para las pruebas de los inputs?
# TODO: La creacion de tareas require rellenar varios parametros, ¿deberiamos crearlos mediante una factoria?

class Repository(Protocol):
    """ Un protocolo puede usarse como interfaz en otros lenguajes
        En este caso estamos definiendo la interfaz Repository junto
        con los metodos que debe tener.
    """

    def getAll(self) -> list[str]:
        pass

    # Ambos metodos estan comentados para mantener la interfaz simple y minimalista
    # def store(self, input: str) -> None:
    #     pass
    #
    # def find(self, input_text) -> bool:
    #     pass

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


class Collect:
    def __init__(self, repository: Repository):
        self._inputs = []
        self.repository = repository

    def _exists(self, text: str) -> bool:
        return self.repository.find(text)

    def input(self, input_text: str):
        if self._exists(input_text):
            return
        else:
            self.repository.store(input_text)
    
    def getAll(self ):
        return self.repository.getAll()


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
