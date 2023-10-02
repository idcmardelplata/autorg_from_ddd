from autorg.domain.protocols.repository import Repository
class Collect:
    def __init__(self, repository: Repository):
        self.repository = repository

    def input(self, input_text: str):
        self.repository.store(input_text)
    
    def getAll(self ):
        return list(set(self.repository.getAll()))
