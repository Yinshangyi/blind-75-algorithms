from abc import ABC, abstractmethod
from typing import List


class MaxSubArrayCalculator(ABC):

    @abstractmethod
    def find_max_sum(self, nums: List[int]) -> int:
        pass
