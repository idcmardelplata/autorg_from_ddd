from autorg.domain.protocols.repository import Repository
from autorg.domain.aggregates.collect import Collect


class EmptyValueError(ValueError):
    pass


class AppInput:
    def __init__(self, repo: Repository):
        self.aggregate = Collect(repo)

    def add_input(self, content: str):
        if content == "":
            raise EmptyValueError()
        self.aggregate.add_input(content)

    def list_inputs(self) -> list | str:
        obtained = self.aggregate.getAll()
        if len(obtained) == 0:
            return "La bandeja de entrada esta vacia"
        else:
            return obtained
