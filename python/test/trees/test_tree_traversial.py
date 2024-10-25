from typing import List

import pytest

from src.trees.traversals.tree_traverser import TreeTraverser
from src.trees.traversals.tree_traverser_fp import TreeTraverserFP
from src.trees.traversals.tree_traverser_imp import TreeTraverserImp
from test.trees.utils import build_tree


@pytest.fixture(params=[
    TreeTraverserImp,
    TreeTraverserFP
])
def tree_traverser(request: pytest.FixtureRequest):
    return request.param()


@pytest.mark.parametrize("tree_nodes, exp_traversal", [
    ([1, 2, 3, 4, 5, None, 6], [4, 2, 5, 1, 3, 6])
])
def test_should_return_the_inorder_traversal(tree_traverser: TreeTraverser,
                                             tree_nodes: List[int],
                                             exp_traversal: List[int]):
    tree = build_tree(tree_nodes)
    traversal = tree_traverser.inorder_traversal(tree)
    assert traversal == exp_traversal


@pytest.mark.parametrize("tree_nodes, exp_traversal", [
    ([1, 2, 3, 4, 5, None, 6], [1, 2, 4, 5, 3, 6])
])
def test_should_return_the_preorder_traversal(tree_traverser: TreeTraverser,
                                              tree_nodes: List[int],
                                              exp_traversal: List[int]):
    tree = build_tree(tree_nodes)
    traversal = tree_traverser.preorder_traversal(tree)
    assert traversal == exp_traversal


@pytest.mark.parametrize("tree_nodes, exp_traversal", [
    ([1, 2, 3, 4, 5, None, 6], [4, 5, 2, 6, 3, 1])
])
def test_should_return_the_postorder_traversal(tree_traverser: TreeTraverser,
                                               tree_nodes: List[int],
                                               exp_traversal: List[int]):
    tree = build_tree(tree_nodes)
    traversal = tree_traverser.postorder_traversal(tree)
    assert traversal == exp_traversal
