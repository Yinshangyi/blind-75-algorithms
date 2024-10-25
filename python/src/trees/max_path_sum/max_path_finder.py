from abc import ABC, abstractmethod
from typing import Optional

from src.trees.utils import TreeNode


class MaxPathFinder(ABC):

    @abstractmethod
    def find_max_path(self, root: Optional[TreeNode]) -> int:
        pass
