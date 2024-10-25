from abc import ABC, abstractmethod
from typing import Optional, List

from src.trees.utils import TreeNode


class LevelOrderTraversal(ABC):

    @abstractmethod
    def get_level_order(self, root: Optional[TreeNode]) -> List[List[int]]:
        pass
