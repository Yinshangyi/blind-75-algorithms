# Definition for a binary tree node.
from typing import Optional

from src.trees.utils import TreeNode


class Solution:
    def isSameTree(self, rootNode1: Optional[TreeNode], rootNode2: Optional[TreeNode]) -> bool:
        if rootNode1 is None and rootNode2 is None:
            return True
        if rootNode1 is None or rootNode2 is None:
            return False
        return rootNode1.val == rootNode2.val \
               and self.isSameTree(rootNode1.left, rootNode2.left) \
               and self.isSameTree(rootNode1.right, rootNode2.right)

