from typing import Optional

from src.trees.is_same_tree.same_tree_finder import SameTreeFinder
from src.trees.utils import TreeNode


class SameTreeFinderFP(SameTreeFinder):

    # @formatter:off
    def is_same_tree(self, root_node1: Optional[TreeNode], root_node2: Optional[TreeNode]) -> bool:
        match (root_node1, root_node2):
            case (_, _) if not root_node1 and not root_node2: return True
            case (_, _) if not root_node1 or not root_node2: return False
            case _:
                return root_node1.val == root_node2.val \
                    and self.is_same_tree(root_node1.left, root_node2.left) \
                    and self.is_same_tree(root_node1.right, root_node2.right)
