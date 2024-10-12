from typing import List

import pytest

from src.arrays.binary_searcher.binary_searcher import BinarySearcher
from src.arrays.binary_searcher.binary_searcher_impl import BinarySearcherImpl


@pytest.fixture(params=[BinarySearcherImpl])
def binary_searcher(request: pytest.FixtureRequest):
    return request.param()


@pytest.mark.parametrize("array, target, expected_index", [
    ([1, 3, 5, 10, 20, 25, 30], 3, 1),
    ([1, 3, 5, 10, 20, 25, 30], 1, 0),
    ([1, 3, 5, 10, 20, 25, 30], 30, 6),
    ([5], 5, 0)
])
def test_searcher_should_return_index_of_target_elemnent(binary_searcher: BinarySearcher, array: List[int], target: int,
                                                         expected_index: int) -> None:
    found_item_index = binary_searcher.binarySearch(array, target)
    assert found_item_index == expected_index


def test_searcher_should_return_neg_1_when_target_not_found(binary_searcher):
    array = [1, 3, 5, 10, 20, 25, 30]
    found_item_index = binary_searcher.binarySearch(array, 28)
    assert found_item_index == -1


def test_searcher_should_return_neg_1_when_empty_arrray_is_provided(binary_searcher):
    array = []
    found_item_index = binary_searcher.binarySearch(array, 3)
    assert found_item_index == -1
