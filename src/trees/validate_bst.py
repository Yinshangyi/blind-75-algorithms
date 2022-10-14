import math
from typing import Optional

from src.trees.utils import TreeNode


class Solution:
    def isNodeValid(self, node: TreeNode, leftBoundary: int, rightBoundary: int) -> bool:
        if not node:
            return True
        if not (leftBoundary < node.val < rightBoundary):
            return False
        return self.isNodeValid(node.left, leftBoundary, node.val) \
               and self.isNodeValid(node.right, node.val, rightBoundary)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isNodeValid(root, -math.inf, math.inf)
