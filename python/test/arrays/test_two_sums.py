from typing import List

import pytest

from src.arrays.two_sums.two_sums_finder import TwoSumsFinder
from src.arrays.two_sums.two_sums_finder_fp import TwoSumsFinderFP
from src.arrays.two_sums.two_sums_finder_imp import TwoSumsFinderImp


@pytest.fixture(params=[
    TwoSumsFinderImp,
    TwoSumsFinderFP
])
def two_sums_finder(request: pytest.FixtureRequest):
    return request.param()


@pytest.mark.parametrize("nums, target, exp_indexes", [
    ([2, 7, 11, 15], 9, [0, 1])
])
def test_should_return_the_indexes_of_two_items_making_the_sum_equal_to_target(two_sums_finder: TwoSumsFinder,
                                                                               nums: List[int],
                                                                               target: int,
                                                                               exp_indexes: List[int]):
    indexes = two_sums_finder.find_two_sums_indexes(nums, target)
    assert sorted(indexes) == exp_indexes
