from typing import List

import pytest

from src.trees.k_smallest_item.k_smallest_item_finder import KSmallestItemFinder
from src.trees.k_smallest_item.k_smallest_item_finder_fp import KSmallestItemFinderFP
from src.trees.k_smallest_item.k_smallest_item_finder_imp import KSmallestItemFinderImp
from test.trees.utils import build_tree


@pytest.fixture(params=[
    KSmallestItemFinderImp,
    KSmallestItemFinderFP
])
def item_finder(request: pytest.FixtureRequest):
    return request.param()


@pytest.mark.parametrize("tree_node, k, exp_smallest_item", [
    ([3, 1, 4, None, 2], 1, 1),
    ([5, 3, 6, 2, 4, None, None, 1], 3, 3),
    ([3, 1, 4, None, 2], 2, 2),
])
def test_should_return_the_nth_smallest_item_in_bst(item_finder: KSmallestItemFinder,
                                                    tree_node: List[int],
                                                    k: int,
                                                    exp_smallest_item: int):
    tree = build_tree([3, 1, 4, None, 2])
    smallest_item = item_finder.kth_smallest(tree, k)
    assert smallest_item == exp_smallest_item
