from typing import Protocol

from autorg.domain.entities.input import Input


class Repository(Protocol):
    """Un protocolo puede usarse como interfaz en otros lenguajes
    En este caso estamos definiendo la interfaz Repository junto
    con los metodos que debe tener.
    """

    def getAll(self) -> list[Input]:
        raise NotImplementedError()

    def store(self, item: Input):
        raise NotImplementedError()
