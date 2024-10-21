from abc import ABC, abstractmethod
from typing import List


class TwoSumsFinder(ABC):

    @abstractmethod
    def find_two_sums_indexes(self, nums: List[int], target: int) -> List[int]:
       pass
