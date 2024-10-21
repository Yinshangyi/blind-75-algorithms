from abc import ABC, abstractmethod
from typing import List


class ProfitFinder(ABC):

    @abstractmethod
    def get_max_profit(self, prices: List[int]) -> int:
        pass
