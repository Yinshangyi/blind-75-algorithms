from typing import Optional

from src.trees.invert_tree.tree_inverter import TreeInverter
from src.trees.utils import TreeNode


class TreeInverterImp(TreeInverter):
    def invert_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        tmp_left_node = root.left
        root.left = root.right
        root.right = tmp_left_node
        self.invert_tree(root.left)
        self.invert_tree(root.right)
        return root
