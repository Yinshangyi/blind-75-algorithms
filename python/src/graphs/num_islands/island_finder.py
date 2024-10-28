from abc import ABC, abstractmethod
from typing import List


class IslandFinder(ABC):

    @abstractmethod
    def get_islands_number(self, grid: List[List[str]]) -> int:
        pass
