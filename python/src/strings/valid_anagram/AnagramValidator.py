from abc import ABC, abstractmethod


class AnagramValidator(ABC):

    @abstractmethod
    def is_anagram(self, str1: str, str2: str) -> bool:
        pass
