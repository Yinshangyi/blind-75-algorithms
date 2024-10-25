from collections import deque
from typing import Optional, List

from src.trees.level_order_traversal.level_order_trav import LevelOrderTraversal
from src.trees.utils import TreeNode


class LevelOrderTraversalImp(LevelOrderTraversal):

    def get_level_order(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels: List[List[int]] = []
        queue: deque[TreeNode] = deque()
        queue.append(root)
        while queue:
            curr_level = []
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                if node:
                    curr_level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if curr_level:
                levels.append(curr_level)
        return levels
