from abc import ABC, abstractmethod
from typing import List


class MaxProductSubArrayFinder(ABC):
    @abstractmethod
    def max_product(self, nums: List[int]):
        pass
