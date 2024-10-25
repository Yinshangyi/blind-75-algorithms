from abc import ABC, abstractmethod
from typing import Optional

from src.trees.utils import TreeNode


class KSmallestItemFinder(ABC):

    @abstractmethod
    def kth_smallest(self, root: Optional[TreeNode], k: int) -> int:
        pass
