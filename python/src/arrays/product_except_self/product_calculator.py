from abc import ABC, abstractmethod
from typing import List


class ProductCalculator(ABC):

    @abstractmethod
    def product_except_self(self, nums: List[int]) -> List[int]:
        pass
