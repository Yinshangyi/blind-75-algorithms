from collections import deque
from typing import Optional

from src.trees.utils import TreeNode


class Solution:
    def addToStackInOrderElements(self, root: Optional[TreeNode], stack: deque) -> deque:
        if root:
            self.addToStackInOrderElements(root.left, stack)
            stack.append(root)
            self.addToStackInOrderElements(root.right, stack)
        return stack

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = deque()
        stackResult = self.addToStackInOrderElements(root, stack)
        kSmallestElement: TreeNode = TreeNode(None)
        while len(stackResult) > 0 and k > 0:
            kSmallestElement = stackResult.popleft()
            k -= 1
        return kSmallestElement.val
