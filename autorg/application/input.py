from autorg.domain.protocols.repository import Repository
from autorg.domain.aggregates.collect import Collect

class AppInput:
    def __init__(self,repo:Repository):
        self.aggregate = Collect(repo)

    def add_input(self,content:str):
        self.aggregate.input(content)
