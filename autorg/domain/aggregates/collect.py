from autorg.domain.protocols.protocols import Repository
class Collect:
    def __init__(self, repository: Repository):
        self.repository = repository

    def _exists(self, text: str) -> bool:
        return self.repository.find(text)

    def input(self, input_text: str):
        if self._exists(input_text):
            return
        else:
            self.repository.store(input_text)
    
    def getAll(self ):
        return self.repository.getAll()
