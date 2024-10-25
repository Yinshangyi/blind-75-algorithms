from abc import abstractmethod
from typing import Optional

from src.trees.utils import TreeNode


class MaxDepthFinder:

    @abstractmethod
    def max_depth(self, root: Optional[TreeNode]) -> int:
        pass