from abc import abstractmethod
from typing import Optional

from src.trees.utils import TreeNode


class TreeInverter:

    @abstractmethod
    def invert_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        pass