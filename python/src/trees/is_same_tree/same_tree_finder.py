from abc import ABC, abstractmethod
from typing import Optional

from src.trees.utils import TreeNode


class SameTreeFinder(ABC):

    @abstractmethod
    def is_same_tree(self, root_node1: Optional[TreeNode], root_node2: Optional[TreeNode]) -> bool:
        pass
