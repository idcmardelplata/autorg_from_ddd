from typing import Protocol

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
