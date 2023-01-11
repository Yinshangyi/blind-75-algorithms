from typing import Optional

from src.trees.utils import TreeNode


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        tmpLeftChild = root.left
        root.left = root.right
        root.right = tmpLeftChild
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
