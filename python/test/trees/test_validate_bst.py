from typing import List

import pytest

from src.trees.validate_bst.bst_validator import BSTValidator
from src.trees.validate_bst.bst_validator_fp import BSTValidatorFP
from test.trees.utils import build_tree


@pytest.fixture(params=[
    BSTValidatorFP
])
def bst_validator(request: pytest.FixtureRequest):
    return request.param()


@pytest.mark.parametrize("tree_node", [
    ([2, 1, 3]),
    ([4, 2, 6, 1, 3, 5, 7])
])
def test_should_return_true_if_bst_is_valid(bst_validator: BSTValidator, tree_node: List[int]):
    tree_node = build_tree(tree_node)
    valid_bst = bst_validator.is_valid_bst(tree_node)
    assert valid_bst


@pytest.mark.parametrize("tree_node", [
    ([5, 1, 4, None, None, 3, 6]),
])
def test_should_return_false_if_bst_is_not_valid(bst_validator: BSTValidator, tree_node: List[int]):
    tree_node = build_tree(tree_node)
    valid_bst = bst_validator.is_valid_bst(tree_node)
    assert not valid_bst
