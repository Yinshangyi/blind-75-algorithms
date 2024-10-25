from typing import Optional, List

from src.trees.traversals.tree_traverser import TreeTraverser
from src.trees.utils import TreeNode


class TreeTraverserFP(TreeTraverser):

    def inorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        return self.inorder_traversal(root.left) + [root.val] + self.inorder_traversal(root.right)

    def preorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        return [root.val] + self.preorder_traversal(root.left) + self.preorder_traversal(root.right)

    def postorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        return self.postorder_traversal(root.left) + self.postorder_traversal(root.right) + [root.val]
