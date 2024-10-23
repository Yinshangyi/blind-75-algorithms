from abc import ABC, abstractmethod
from typing import List


class MostWaterFinder(ABC):

    @abstractmethod
    def max_area(self, heights: List[int]) -> int:
       pass