from typing import Optional

from src.trees.utils import TreeNode


class Solution:
    def isSameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]):
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        return root.val == subRoot.val \
               and self.isSameTree(root.left, subRoot.left) \
               and self.isSameTree(root.right, subRoot.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True
        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
