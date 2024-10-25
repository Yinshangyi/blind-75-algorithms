from abc import abstractmethod
from typing import Optional

from src.trees.utils import TreeNode


class BSTValidator:

    @abstractmethod
    def is_valid_bst(self, root: Optional[TreeNode]) -> bool:
        pass
