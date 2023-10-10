from autorg.domain.aggregates.collect import Collect
from autorg.domain.protocols.repository import Repository
from autorg.application.dtos.input_dto import InputDto
from tests.helpers.repository import InMemoryRepository


class CollectFactory:
    def __init__(self):
        pass

    @staticmethod
    def createWithInput(repository: Repository = InMemoryRepository()):
        collect = Collect(repository)
        collect.add_input(InputDto(None,"some random input",None))
        return collect

    @staticmethod
    def createDuplicateInputs(repository: Repository = InMemoryRepository()):
        collect = Collect(repository)
        collect.add_input(InputDto(None,"duplicate input",None))
        collect.add_input(InputDto(None,"duplicate input",None))
        return collect

    @staticmethod
    def createManyInputs(count: int = 2, repository: Repository = InMemoryRepository()):
        collect = Collect(repository)
        for n in range(0, count):
            collect.add_input(InputDto(None,f"input {n}",None))
        return collect
