from autorg.domain.entities.base import Entity
import datetime


class Input(Entity):
    def __init__(
        self, content: str, id: int = 0, creation_date=datetime.datetime.now()
    ) -> None:
        self._content = content
        self._date = creation_date
        self._id = id

    def id(self) -> int:
        return self._id

    def creation_date(self):
        return self._date

    def value(self) -> dict:
        return {"creation_date": self._date, "content": self._content}

    def content(self):
        return self._content

    def __eq__(self, other):
        return self.id() == other.id()
