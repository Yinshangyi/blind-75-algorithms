import math
from typing import Optional

from src.trees.utils import TreeNode
from src.trees.validate_bst.bst_validator import BSTValidator


class BSTValidatorFP(BSTValidator):

    def is_valid_bst(self, root: Optional[TreeNode]) -> bool:
        def helper(_root: Optional[TreeNode], left_bound: float, right_bound: float) -> bool:
            if not _root:
                return True
            if not (left_bound < _root.val < right_bound):
                return False
            return helper(_root.left, left_bound, _root.val) and helper(_root.right, _root.val, right_bound)

        return helper(root, -math.inf, math.inf)
