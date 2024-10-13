from typing import List

import pytest

from src.arrays.max_prod_sub_array.max_prod_finder import MaxProductSubArrayFinder
from src.arrays.max_prod_sub_array.max_prod_finder_fp_rec import MaxProductSubArrayFinderFPRec
from src.arrays.max_prod_sub_array.max_prod_finder_fp_reduce import MaxProductSubArrayFinderFPReduce
from src.arrays.max_prod_sub_array.max_prod_finder_imp import MaxProductSubArrayFinderImp


@pytest.fixture(params=[
    MaxProductSubArrayFinderImp,
    MaxProductSubArrayFinderFPRec,
    MaxProductSubArrayFinderFPReduce]
)
def max_product_subarray_finder(request: pytest.FixtureRequest):
    return request.param()


@pytest.mark.parametrize("nums, exp_product", [
    ([2, 3, -2, 4], 6),
    ([-2, 0, -1], 0),
    ([-4, -3, -2], 12),
    ([-2, 3, -4], 24)
])
def test_should_return_the_max_product_sub_array(max_product_subarray_finder: MaxProductSubArrayFinder, nums: List[int],
                                                 exp_product: int):
    max_product = max_product_subarray_finder.max_product(nums)
    assert max_product == exp_product
