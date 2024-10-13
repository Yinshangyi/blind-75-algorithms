from typing import List

import pytest

from src.arrays.min_rotated_array.min_rotate_array_fp import MinRotatedArrayFinderFP
from src.arrays.min_rotated_array.min_rotated_array import MinRotatedArrayFinder
from src.arrays.min_rotated_array.min_rotated_array_imp import MinRotatedArrayFinderImp


@pytest.fixture(params=[
    MinRotatedArrayFinderImp,
    MinRotatedArrayFinderFP
]
)
def min_finder(request: pytest.FixtureRequest):
    return request.param()


@pytest.mark.parametrize("array, exp_min", [
    ([3, 4, 5, 1, 2], 1),
    ([4, 5, 6, 7, 0, 1, 2], 0),
    ([20, 30, 10, 11, 12], 10)
])
def test_should_return_the_lowest_item(min_finder: MinRotatedArrayFinder, array: List[int], exp_min: int):
    actual_min = min_finder.find_min(array)
    assert actual_min == exp_min
