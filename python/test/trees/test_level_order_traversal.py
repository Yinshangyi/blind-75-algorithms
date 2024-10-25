from typing import List

import pytest

from src.trees.level_order_traversal.level_order_trav import LevelOrderTraversal
from src.trees.level_order_traversal.level_order_trav_fp import LevelOrderTraversalFP
from src.trees.level_order_traversal.level_order_trav_imp import LevelOrderTraversalImp
from test.trees.utils import build_tree


@pytest.fixture(params=[
    LevelOrderTraversalImp,
    LevelOrderTraversalFP
])
def level_order_retriever(request: pytest.FixtureRequest):
    return request.param()


@pytest.mark.parametrize("tree_node, exp_levels", [
    ([1], [[1]]),
    ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]])
])
def test_should_return_tree_order_traversal(level_order_retriever: LevelOrderTraversal,
                                            tree_node: List[int],
                                            exp_levels: List[List[int]]):
    tree = build_tree(tree_node)
    levels = level_order_retriever.get_level_order(tree)
    assert levels == exp_levels
