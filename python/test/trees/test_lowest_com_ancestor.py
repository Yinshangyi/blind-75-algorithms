from typing import List

import pytest

from src.trees.lowest_com_ancestor.ancestor_finder import LowestComAncestorFinder
from src.trees.lowest_com_ancestor.ancestor_finder_fp import LowestComAncestorFinderFP
from src.trees.lowest_com_ancestor.ancestor_finder_imp import LowestComAncestorFinderImp
from src.trees.utils import TreeNode
from test.trees.utils import build_tree


@pytest.fixture(params=[
    LowestComAncestorFinderImp,
    LowestComAncestorFinderFP
])
def ancestor_finder(request: pytest.FixtureRequest):
    return request.param()


@pytest.mark.parametrize("tree_node, node1_val, node2_val, exp_node_val", [
    ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 8, 6),
    ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 4, 2),
    ([2, 1], 2, 1, 2),
    ([3, 1, 8, None, None, 5, 10, 4, 6, 9, 11], 9, 11, 10)
])
def test_should_return_the_lowest_common_ancestor(ancestor_finder: LowestComAncestorFinder,
                                                  tree_node: List[int], node1_val: int, node2_val: int,
                                                  exp_node_val: int):
    tree = build_tree(tree_node)
    node1 = TreeNode(node1_val)
    node2 = TreeNode(node2_val)
    ancestor_node = ancestor_finder.lowest_common_ancestor(tree, node1, node2)
    assert ancestor_node.val == exp_node_val
