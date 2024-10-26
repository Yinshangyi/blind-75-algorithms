from abc import abstractmethod

from src.trees.utils import TreeNode


class LowestComAncestorFinder:

    @abstractmethod
    def lowest_common_ancestor(self, root: TreeNode, node1: TreeNode, node2: TreeNode) -> TreeNode:
        pass