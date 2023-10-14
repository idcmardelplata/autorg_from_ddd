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

    #NOTE: Dado que collect es una entidad que tiene como finalidad
    # servir como punto de entrada al dominio, los datos que deben tratarse
    # en los metodos que expone deben ser datos primitivos.
    def add_input(self, data: str):
         if len(self._inputs) == 0:
             self._inputs = self._repo.getAll()

         if not self._isDuplicate(data):
            inp = self._make_input(data)
            self._repo.store(inp)
            self._inputs.append(inp)
         else:
            raise DuplicateInputError("Input exists")

    def getAll(self) -> list[Input]:
        # NOTE: Dado que  collect es un aggregate debe retornar datos primitivos
        # o datos del dominio, los dtos deben ser creados y asignados en la capa de aplicacion 
        # pero nunca retornar dtos desde el dominio.
        return self._inputs if len(self._inputs) > 0 else self._repo.getAll()

    def _gen_input_id(self) -> int:
        return (
            max([inp.id() for inp in self._inputs]) + 1 if len(self._inputs) > 0 else 0
        )

    def _isDuplicate(self, content) -> bool:
        return content in [inp.content() for inp in self._inputs] 

    def _make_input(self, content: str) -> Input:
        return Input(content=content, id=self._gen_input_id())
    
