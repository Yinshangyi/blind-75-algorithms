from abc import ABC, abstractmethod
from typing import Optional

from src.trees.utils import TreeNode


class SubtreeFinder(ABC):

    @abstractmethod
    def is_subtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        pass
