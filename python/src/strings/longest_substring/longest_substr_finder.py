from abc import ABC, abstractmethod


class LongestSubstringFinder(ABC):

    @abstractmethod
    def get_length_of_longest_substring(self, input_string: str) -> int:
        pass