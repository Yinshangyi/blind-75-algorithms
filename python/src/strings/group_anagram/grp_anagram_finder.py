from abc import ABC, abstractmethod
from typing import List


class GroupAnagramFinder(ABC):

    @abstractmethod
    def group_anagrams(self, words: List[str]) -> List[List[str]]:
        pass
