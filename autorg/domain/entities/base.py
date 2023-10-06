from abc import ABC, abstractmethod


class Entity(ABC):
    @abstractmethod
    def id(self) -> int:
        pass
