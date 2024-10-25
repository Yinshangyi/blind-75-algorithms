from abc import ABC, abstractmethod
from typing import Optional, List

from src.trees.utils import TreeNode


class TreeTraverser(ABC):

    @abstractmethod
    def inorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        pass

    @abstractmethod
    def preorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        pass

    @abstractmethod
    def postorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        pass
