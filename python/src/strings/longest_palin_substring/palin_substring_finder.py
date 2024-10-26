from abc import ABC, abstractmethod


class LongestPalindromeSubstringFinder(ABC):

    @abstractmethod
    def longest_palindrome(self, string: str) -> str:
        pass
