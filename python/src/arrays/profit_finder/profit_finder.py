from abc import ABC, abstractmethod
from typing import List


class ProfitFinder(ABC):

    @abstractmethod
    def maxProfit(self, prices: List[int]) -> int:
        pass
