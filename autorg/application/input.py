from autorg.domain.entities.input import Input
from autorg.application.dtos.input_dto import InputDto
from autorg.domain.protocols.repository import Repository
from autorg.domain.aggregates.collect import Collect



class EmptyValueError(ValueError):
    pass


class AppInput:
    def __init__(self, repo: Repository):
        self.aggregate = Collect(repo)

    def add_input(self, content: str):
        if content == "":
            raise EmptyValueError()
        self.aggregate.add_input(content)

    def list_inputs(self) -> list[InputDto]:
        return [InputDto(input.id(), input.content(), input.creation_date()) for input in self.aggregate.getAll()]
