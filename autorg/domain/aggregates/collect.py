from autorg.domain.entities.input import Entity, Input
from autorg.domain.protocols.repository import Repository
from autorg.infrastructure.adapters.csvrepository import CsvRepository

class Collect(Entity):
    def __init__(self, repo: Repository = CsvRepository()):
        self._id = 0
        self._inputs: list[Input] = []
        self._repo = repo

    def id(self) -> int:
        return self._id

    def add_input(self, content: str):
        contents = [inp.value()["content"] for inp in self._inputs]
        if not content in contents:
            inp = Input(content=content, id=self._gen_input_id())
            self._inputs.append(inp)
            self._repo.store(inp)

    def getAll(self) -> list[Input]:
        # TODO: Esto tiene que traer los inputs desde un repositorio, reconstruirlos y retornar una list[Input]

        return self._inputs if len(self._inputs) > 0 else self._repo.getAll()

    def _gen_input_id(self) -> int:
        return (
            max([inp.id() for inp in self._inputs]) + 1 if len(self._inputs) > 0 else 0
        )
