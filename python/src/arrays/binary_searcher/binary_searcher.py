from abc import abstractmethod
from typing import List


class BinarySearcher:
    @abstractmethod
    def binarySearch(self, nums: List[int], target: int) -> int:
        pass
