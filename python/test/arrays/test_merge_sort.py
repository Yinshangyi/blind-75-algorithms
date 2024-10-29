from typing import List

import pytest

from src.arrays.merge_sort.merge_sort import MergeSort
from src.arrays.merge_sort.merge_sort_imp import MergeSortImp


@pytest.fixture(params=[
    MergeSortImp
]
)
def merger(request: pytest.FixtureRequest):
    return request.param()


@pytest.mark.parametrize("array, exp_sorted_array", [
    ([1, 3, 4, 5, 6, 8, 2, 7, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9])
])
def test_should_return_the_sorted_array(merger: MergeSort, array: List[int], exp_sorted_array: List[int]):
    assert merger.sort(array) == exp_sorted_array
