from typing import Optional, List

from src.trees.k_smallest_item.k_smallest_item_finder import KSmallestItemFinder
from src.trees.utils import TreeNode


class KSmallestItemFinderFP(KSmallestItemFinder):

    def kth_smallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder_traversal(_root: Optional[TreeNode]) -> List[int]:
            if not _root:
                return []
            return inorder_traversal(_root.left) + [_root.val] + inorder_traversal(_root.right)

        traversal = inorder_traversal(root)
        return traversal[k - 1]
