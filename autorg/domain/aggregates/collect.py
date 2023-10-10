from autorg.domain.entities.input import Entity, Input
from autorg.application.dtos.input_dto import InputDto
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

    def add_input(self, input_dto: InputDto):
         if len(self._inputs) == 0:
             self._inputs = self._repo.getAll()

         if not self._isDuplicate(input_dto.content):
            inp = self._make_input(input_dto.content)
            self._repo.store(inp)
            self._inputs.append(inp)
         else:
            raise DuplicateInputError("Input exists")

    def getAll(self) -> list[InputDto]:
        return self._inputs if len(self._inputs) > 0 else self._repo.getAll()

    def _gen_input_id(self) -> int:
        return (
            max([inp.id() for inp in self._inputs]) + 1 if len(self._inputs) > 0 else 0
        )

    def _isDuplicate(self, content) -> bool:
        return content in [inp.content() for inp in self._inputs] 

    def _make_input(self, content) -> Input:
        return Input(content=content, id=self._gen_input_id())
    
