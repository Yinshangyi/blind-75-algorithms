from typing import List

import pytest

from src.trees.max_depth.max_depth_finder import MaxDepthFinder
from src.trees.max_depth.max_depth_finder_imp import MaxDepthFinderImp
from test.trees.utils import build_tree


@pytest.fixture(params=[
    MaxDepthFinderImp
])
def max_depth_finder(request: pytest.FixtureRequest):
    return request.param()


@pytest.mark.parametrize("tree_node, exp_depth", [
    ([3, 9, 20, None, None, 15, 7], 3),
    ([1, None, 2], 2)
])
def test_should_return_the_max_depth_of_the_tree(max_depth_finder: MaxDepthFinder, tree_node: List[int],
                                                 exp_depth: List[int]):
    tree_node = build_tree([3, 9, 20, None, None, 15, 7])
    tree_depth = max_depth_finder.max_depth(tree_node)
    assert tree_depth == 3
