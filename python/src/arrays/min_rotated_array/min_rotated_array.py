from abc import ABC, abstractmethod
from typing import List


class MinRotatedArrayFinder(ABC):

    @abstractmethod
    def find_min(self, nums: List[int]) -> int:
        pass