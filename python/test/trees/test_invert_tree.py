from typing import List

import pytest

from src.trees.invert_tree.tree_inverter import TreeInverter
from src.trees.invert_tree.tree_inverter_imp import TreeInverterImp
from test.trees.utils import build_tree, is_same_tree


@pytest.fixture(params=[
    TreeInverterImp
])
def tree_inverter(request: pytest.FixtureRequest):
    return request.param()


@pytest.mark.parametrize("nodes, exp_nodes", [
    ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
    ([2, 1, 3], [2, 3, 1]),
    ([], [])
])
def test_should_return_a_inverted_tree(tree_inverter: TreeInverter, nodes: List[int], exp_nodes: List[int]):
    tree_node = build_tree(nodes)
    inverted_tree_node = tree_inverter.invert_tree(tree_node)
    expected_inverted_tree_node = build_tree(exp_nodes)
    assert is_same_tree(inverted_tree_node, expected_inverted_tree_node) == True
