from typing import List

import pytest

from src.trees.is_subtree.subtree_finder import SubtreeFinder
from src.trees.is_subtree.subtree_finder_imp import SubtreeFinderImp
from test.trees.utils import build_tree


@pytest.fixture(params=[
    SubtreeFinderImp
])
def subtree_finder(request: pytest.FixtureRequest):
    return request.param()


@pytest.mark.parametrize("tree_node1, tree_node2", [
    ([3, 4, 5, 1, 2], [4, 1, 2]),
])
def test_should_return_true_if_the_first_tree_is_subtree_of_the_second_tree(subtree_finder: SubtreeFinder,
                                                                            tree_node1: List[int],
                                                                            tree_node2: List[int]):
    tree_node = build_tree(tree_node1)
    small_tree_node = build_tree(tree_node2)
    sub_tree = subtree_finder.is_subtree(tree_node, small_tree_node)
    assert sub_tree


@pytest.mark.parametrize("tree_node1, tree_node2", [
    ([3, 4, 5, 1, 2, None, None, None, None, 0], [4, 1, 2])
])
def test_should_return_false_if_the_first_tree_is_not_subtree_of_the_second_tree(subtree_finder: SubtreeFinder,
                                                                                 tree_node1: List[int],
                                                                                 tree_node2: List[int]):
    tree_node = build_tree(tree_node1)
    small_tree_node = build_tree(tree_node2)
    sub_tree = subtree_finder.is_subtree(tree_node, small_tree_node)
    assert not sub_tree
