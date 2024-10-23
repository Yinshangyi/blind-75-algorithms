from typing import List

import pytest

from src.arrays.three_sums.three_sums_finder import ThreeSumsFinder
from src.arrays.three_sums.three_sums_finder_imp import ThreeSumsFinderImp


@pytest.fixture(params=[
    ThreeSumsFinderImp
])
def three_sums_finder(request: pytest.FixtureRequest):
    return request.param()


@pytest.mark.parametrize("nums, target, exp_result", [
    ([-1, 0, 1, 2, -1, -4], 0, [[-1, -1, 2], [-1, 0, 1]])
])
def test_should_return_the_indexes_of_three_items_making_the_sum_equal_to_target(three_sums_finder: ThreeSumsFinder,
                                                                                 nums: List[int],
                                                                                 target: int,
                                                                                 exp_result: List[List[int]]):
    result = three_sums_finder.three_sum(nums, target)
    assert result == exp_result
