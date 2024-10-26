from abc import ABC, abstractmethod


class PalindromeValidator(ABC):

    @abstractmethod
    def is_palindrome(self, string: str) -> bool:
        pass
