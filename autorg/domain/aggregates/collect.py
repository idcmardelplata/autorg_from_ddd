from autorg.domain.entities.input import Entity, Input
from autorg.domain.protocols.repository import Repository
from autorg.infrastructure.adapters.csvrepository import CsvRepository

class DuplicateInputError(Exception):
    pass

class Collect(Entity):
    def __init__(self, repo: Repository = CsvRepository()):
        self._id = 0
        self._inputs: list[Input] = []
        self._repo = repo

    def id(self) -> int:
        return self._id

    def add_input(self, content: str):
         if len(self._inputs) == 0:
             self._inputs = self._repo.getAll()

         if not self._isDuplicate(content):
            inp = self._make_input(content)
            self._repo.store(inp)
            self._inputs.append(inp)
         else:
            raise DuplicateInputError("Input exists")

    def getAll(self) -> list[Input]:
        return self._inputs if len(self._inputs) > 0 else self._repo.getAll()

    def _gen_input_id(self) -> int:
        return (
            max([inp.id() for inp in self._inputs]) + 1 if len(self._inputs) > 0 else 0
        )

    def _isDuplicate(self, content) -> bool:
        return content in [inp.content() for inp in self._inputs] 

    def _make_input(self, content) -> Input:
        return Input(content=content, id=self._gen_input_id())
    
