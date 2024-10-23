from abc import abstractmethod
from typing import List


class ThreeSumsFinder:

    @abstractmethod
    def three_sum(self, nums: List[int], target: int) -> List[List[int]]:
        pass
