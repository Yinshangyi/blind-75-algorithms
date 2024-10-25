from typing import Optional

from src.trees.max_depth.max_depth_finder import MaxDepthFinder
from src.trees.utils import TreeNode


class MaxDepthFinderImp(MaxDepthFinder):

    def max_depth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1 + max(self.max_depth(root.left), self.max_depth(root.right))
