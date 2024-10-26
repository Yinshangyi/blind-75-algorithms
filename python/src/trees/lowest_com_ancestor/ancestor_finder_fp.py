from src.trees.lowest_com_ancestor.ancestor_finder import LowestComAncestorFinder
from src.trees.utils import TreeNode


class LowestComAncestorFinderFP(LowestComAncestorFinder):
    def lowest_common_ancestor(self, root: TreeNode, node1: TreeNode, node2: TreeNode) -> TreeNode:
        if root.val > node1.val and root.val > node2.val:
            return self.lowest_common_ancestor(root.left, node1, node2)
        elif root.val < node1.val and root.val < node2.val:
            return self.lowest_common_ancestor(root.right, node1, node2)
        else:
            return root
