import datetime
from dataclasses import dataclass

from autorg.domain.entities.input import Input

@dataclass
class InputDto():
    id: int
    content: str
    creation_date: datetime.datetime
