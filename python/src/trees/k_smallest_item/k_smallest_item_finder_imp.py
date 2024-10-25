from typing import Optional, List

from src.trees.k_smallest_item.k_smallest_item_finder import KSmallestItemFinder
from src.trees.utils import TreeNode


class KSmallestItemFinderImp(KSmallestItemFinder):

    def in_order_traversal(self, root: Optional[TreeNode], traversal: List[int]):
        if root is None:
            return
        self.in_order_traversal(root.left, traversal)
        traversal.append(root.val)
        self.in_order_traversal(root.right, traversal)

    def kth_smallest(self, root: Optional[TreeNode], k: int) -> int:
        traversal = []
        self.in_order_traversal(root, traversal)
        return traversal[k-1]
