from typing import List

import pytest

from src.trees.is_same_tree.same_tree_finder import SameTreeFinder
from src.trees.is_same_tree.same_tree_finder_fp import SameTreeFinderFP
from src.trees.is_same_tree.same_tree_finder_imp import SameTreeFinderImp
from test.trees.utils import build_tree


@pytest.fixture(params=[
    SameTreeFinderImp,
    SameTreeFinderFP
])
def subtree_finder(request: pytest.FixtureRequest):
    return request.param()


@pytest.mark.parametrize("tree_node1, tree_node2", [
    ([1, 2, 3], [1, 2, 3]),
])
def test_should_return_true_if_two_trees_are_equal(subtree_finder: SameTreeFinder, tree_node1: List[int],
                                                   tree_node2: List[int]):
    tree1 = build_tree(tree_node1)
    tree2 = build_tree(tree_node2)
    is_same_tree = subtree_finder.is_same_tree(tree1, tree2)
    assert is_same_tree


@pytest.mark.parametrize("tree_node1, tree_node2", [
    ([1, 2], [1, None, 2]),
])
def test_should_return_false_if_two_trees_are_not_equal(subtree_finder: SameTreeFinder, tree_node1: List[int],
                                                        tree_node2: List[int]):
    tree1 = build_tree(tree_node1)
    tree2 = build_tree(tree_node2)
    is_same_tree = subtree_finder.is_same_tree(tree1, tree2)
    assert not is_same_tree
