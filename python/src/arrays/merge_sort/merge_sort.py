from abc import ABC, abstractmethod
from typing import List


class MergeSort(ABC):

    @abstractmethod
    def sort(self, array: List[int]) -> List[int]:
        pass