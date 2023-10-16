from autorg.domain.aggregates.collect import Collect
from autorg.domain.entities.input import Input
from autorg.domain.protocols.repository import Repository
from tests.helpers.repository import InMemoryRepository

class CollectFactory:
    def __init__(self):
        pass

    @staticmethod
    def createWithInput(repository: Repository = InMemoryRepository()):
        collect = Collect(repository)
        collect.add_input(Input("some random input"))
        return collect

    @staticmethod
    def createDuplicateInputs(repository: Repository = InMemoryRepository()):
        collect = Collect(repository)
        collect.add_input(Input("duplicate input"))
        collect.add_input(Input("duplicate input"))
        return collect

    @staticmethod
    def createManyInputs(count: int = 2, repository: Repository = InMemoryRepository()):
        collect = Collect(repository)
        for n in range(0, count):
            collect.add_input(Input(f"input {n}"))
        return collect
