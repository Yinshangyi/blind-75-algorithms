from abc import ABC, abstractmethod
from typing import List


class RotatedArrayFinder(ABC):

    @abstractmethod
    def search(self, nums: List[int], target: int) -> int:
        pass
