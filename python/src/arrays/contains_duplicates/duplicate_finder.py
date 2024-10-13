from abc import ABC, abstractmethod
from typing import List


class DuplicateFinder(ABC):

    @abstractmethod
    def contains_duplicate(self, nums: List[int]) -> bool:
        pass


