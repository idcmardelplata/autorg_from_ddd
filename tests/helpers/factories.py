from autorg.domain.aggregates.collect import Collect
from autorg.domain.protocols.repository import Repository
from tests.helpers.repository import InMemoryRepository


class CollectFactory:
    def __init__(self):
        pass

    @staticmethod
    def createWithInput(repository: Repository = InMemoryRepository()):
        collect = Collect(repository)
        collect.add_input("some random input")
        return collect

    @staticmethod
    def createDuplicateInputs(repository: Repository = InMemoryRepository()):
        collect = Collect(repository)
        collect.add_input("duplicate input")
        collect.add_input("duplicate input")
        return collect

    @staticmethod
    def createManyInputs(count: int = 2, repository: Repository = InMemoryRepository()):
        collect = Collect(repository)
        for n in range(0, count):
            collect.add_input(f"input {n}")
        return collect
