from src.trees.utils import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, node1: TreeNode, node2: TreeNode) -> TreeNode:
        currentNode = root
        while currentNode:
            if node1.val > currentNode.val and node2.val > currentNode.val:
                currentNode = currentNode.right
            elif node1.val < currentNode.val and node2.val < currentNode.val:
                currentNode = currentNode.left
            else:
                return currentNode
