from typing import Optional

from src.trees.is_same_tree.same_tree_finder import SameTreeFinder
from src.trees.utils import TreeNode


class SameTreeFinderImp(SameTreeFinder):

    def is_same_tree(self, root_node1: Optional[TreeNode], root_node2: Optional[TreeNode]) -> bool:
        if root_node1 is None and root_node2 is None:
            return True
        if root_node1 is None or root_node2 is None:
            return False
        return root_node1.val == root_node2.val \
            and self.is_same_tree(root_node1.left, root_node2.left) \
            and self.is_same_tree(root_node1.right, root_node2.right)
