from abc import ABC, abstractmethod


class PalindromeSubstringFinder(ABC):

    @abstractmethod
    def count_substrings(self, string: str) -> int:
        pass
