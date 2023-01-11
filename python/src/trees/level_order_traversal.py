from collections import deque
from typing import Optional, List

from src.trees.utils import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        queue = deque()
        queue.append(root)

        while queue:
            level = []
            levelSize = len(queue)
            for i in range(levelSize):
                node: TreeNode = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                levels.append(level)

        return levels
