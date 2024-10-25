from typing import Optional, List

from src.trees.traversals.tree_traverser import TreeTraverser
from src.trees.utils import TreeNode


class TreeTraverserImp(TreeTraverser):
    def inorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        def helper(_root: Optional[TreeNode], traversal: List[int]):
            if _root is None:
                return
            helper(_root.left, traversal)
            traversal.append(_root.val)
            helper(_root.right, traversal)

        traversal = []
        helper(root, traversal)
        return traversal

    def preorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        def helper(_root: Optional[TreeNode], traversal: List[int]):
            if _root is None:
                return
            traversal.append(_root.val)
            helper(_root.left, traversal)
            helper(_root.right, traversal)

        traversal = []
        helper(root, traversal)
        return traversal

    def postorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        def helper(_root: Optional[TreeNode], traversal: List[int]):
            if _root is None:
                return
            helper(_root.left, traversal)
            helper(_root.right, traversal)
            traversal.append(_root.val)

        traversal = []
        helper(root, traversal)
        return traversal
