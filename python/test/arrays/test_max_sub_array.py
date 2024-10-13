from typing import List

import pytest

from src.arrays.max_sub_array.max_sub_array import MaxSubArrayCalculator
from src.arrays.max_sub_array.max_sub_array_fp_rec import MaxSubArrayCalculatorFPRec
from src.arrays.max_sub_array.max_sub_array_fp_reduce import MaxSubArrayCalculatorFPReduce
from src.arrays.max_sub_array.max_sub_array_imp import MaxSubArrayCalculatorImp


@pytest.fixture(params=[
    MaxSubArrayCalculatorImp,
    MaxSubArrayCalculatorFPRec,
    MaxSubArrayCalculatorFPReduce
]
)
def sum_calculator(request: pytest.FixtureRequest):
    return request.param()


@pytest.mark.parametrize("array, exp_sum", [
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
    ([5, 4, -1, 7, 8], 23),
    ([1], 1),
    ([-1], -1)
])
def test_should_return_the_max_sum(sum_calculator: MaxSubArrayCalculator, array: List[int], exp_sum: int):
    max_sum = sum_calculator.find_max_sum(array)
    assert max_sum == exp_sum
