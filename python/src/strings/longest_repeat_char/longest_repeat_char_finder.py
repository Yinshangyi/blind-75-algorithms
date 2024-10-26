from abc import ABC, abstractmethod


class LongestRepeatCharFinder(ABC):

    @abstractmethod
    def get_longest_character_with_replacement(self, string: str, target: int) -> int:
        pass
