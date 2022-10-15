from collections import deque
from typing import Optional

from src.trees.utils import TreeNode


class Solution:
    def addToStackLeftElements(self, root: Optional[TreeNode], stack: deque) -> deque:
        if root:
            self.addToStackLeftElements(root.left, stack)
            stack.append(root)
        return stack

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = deque()
        stackResult = self.addToStackLeftElements(root, stack)
        kSmallestElement: TreeNode = TreeNode(None)
        while len(stackResult) > 0 and k > 0:
            kSmallestElement = stackResult.popleft()
            k -= 1
            if k > 0:
                kSmallestElement = kSmallestElement.right
                if kSmallestElement:
                    k -= 1
        return kSmallestElement.val
