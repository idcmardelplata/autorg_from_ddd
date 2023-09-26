from autorg.domain.aggregates.collect import Collect
from autorg.domain.protocols.protocols import Repository
from tests.helpers.repository import InMemoryRepository

class CollectFactory:
    def __init__(self):
        pass

    @staticmethod
    def create():
        repo = InMemoryRepository()
        return Collect(repo)
