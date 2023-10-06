import datetime
from dataclasses import dataclass

from autorg.domain.entities.input import Input

@dataclass
class InputDto():
    id: int
    content: str
    creation_date: datetime.datetime

def make_dto_from_input(inp: Input) -> InputDto:
    return InputDto(id=inp.id(), content=inp.content(), creation_date=inp.creation_date())

# def make_input_from_dto(dto: InputDto) -> Input:
#     return Input(id = dto.id, content= dto.content, creation_date=dto.creation_date)
