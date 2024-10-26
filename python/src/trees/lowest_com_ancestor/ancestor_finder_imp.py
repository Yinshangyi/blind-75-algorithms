from src.trees.lowest_com_ancestor.ancestor_finder import LowestComAncestorFinder
from src.trees.utils import TreeNode


class LowestComAncestorFinderImp(LowestComAncestorFinder):
    def lowest_common_ancestor(self, root: TreeNode, node1: TreeNode, node2: TreeNode) -> TreeNode:
        current_node = root
        while current_node:
            if current_node.val < node1.val and current_node.val < node2.val:
                current_node = current_node.right
            elif current_node.val > node1.val and current_node.val > node2.val:
                current_node = current_node.left
            else:
                return current_node
