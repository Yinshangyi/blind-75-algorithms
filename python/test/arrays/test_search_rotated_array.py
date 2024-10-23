from typing import List

import pytest

from src.arrays.search_rotated_array.rotated_array_finder import RotatedArrayFinder
from src.arrays.search_rotated_array.rotated_array_finder_imp import RotatedArrayFinderImp


@pytest.fixture(params=[
    RotatedArrayFinderImp,
])
def finder(request: pytest.FixtureRequest):
    return request.param()


@pytest.mark.parametrize("nums, target, exp_index", [
    ([4, 5, 6, 7, 0, 1, 2], 0, 4),
    ([4, 5, 6, 7, 0, 1, 2], 5, 1)
])
def test_should_return_the_index_of_given_target(finder: RotatedArrayFinder, nums: List[int], target: int,
                                                 exp_index: int):
    found_item = finder.search(nums, target)
    assert found_item == exp_index


@pytest.mark.parametrize("nums, target, exp_index", [
    ([4, 5, 6, 7, 0, 1, 2], 3, -1),
    ([4, 5, 6, 7, 0, 1, 2], 8, -1)
])
def test_should_return_minus_1_when_the_target_is_not_found(finder: RotatedArrayFinder, nums: List[int], target: int,
                                                            exp_index: int):
    found_item = finder.search(nums, target)
    assert found_item == exp_index
