import itertools
from typing import Optional, List

from src.trees.level_order_traversal.level_order_trav import LevelOrderTraversal
from src.trees.utils import TreeNode


class LevelOrderTraversalFP(LevelOrderTraversal):

    def get_level_order(self, root: Optional[TreeNode]) -> List[List[int]]:
        def traverse_levels(queue: List[Optional[TreeNode]]) -> List[List[int]]:
            if not queue:
                return []
            nodes = [node for node in queue if node is not None]
            curr_level = [node.val for node in nodes]
            new_queue = [[node.left, node.right] for node in nodes]
            new_queue_flatten = list(itertools.chain.from_iterable(new_queue))
            return [curr_level] + traverse_levels(new_queue_flatten)

        levels = traverse_levels([root])
        return [level for level in levels if level]
