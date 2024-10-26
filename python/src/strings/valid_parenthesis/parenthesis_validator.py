from abc import ABC, abstractmethod


class ParenthesisValidator(ABC):

    @abstractmethod
    def is_valid(self, string: str) -> bool:
        pass