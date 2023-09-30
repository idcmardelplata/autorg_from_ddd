from autorg.domain.protocols.repository import Repository
from autorg.domain.aggregates.collect import Collect

class EmptyValueError(ValueError):
    pass

class AppInput:
    def __init__(self,repo:Repository):
        self.aggregate = Collect(repo)

    def add_input(self,content:str):
        if content == '':
            raise EmptyValueError()
        self.aggregate.input(content)
