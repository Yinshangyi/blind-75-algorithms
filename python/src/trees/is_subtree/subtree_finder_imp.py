from typing import Optional

from src.trees.is_subtree.subtree_finder import SubtreeFinder
from src.trees.utils import TreeNode


class SubtreeFinderImp(SubtreeFinder):

    def is_subtree(self, root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.is_same_tree(root, sub_root):
            return True
        return self.is_same_tree(root.left, sub_root) \
            or self.is_same_tree(root.right, sub_root)

    def is_same_tree(self, root: Optional[TreeNode], sub_root: Optional[TreeNode]):
        if root is None and sub_root is None:
            return True
        if root is None or sub_root is None:
            return False
        return root.val == sub_root.val \
            and self.is_same_tree(root.left, sub_root.left) \
            and self.is_same_tree(root.right, sub_root.right)
