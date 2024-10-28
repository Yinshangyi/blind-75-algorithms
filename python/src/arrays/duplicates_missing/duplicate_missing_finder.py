from abc import ABC, abstractmethod
from typing import List


class DuplicateAndMissingFinder(ABC):

    @abstractmethod
    def find_duplicate_and_missing_value(self, nums: List[int]) -> tuple[int, int]:
        pass