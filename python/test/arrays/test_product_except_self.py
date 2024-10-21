from typing import List

import pytest

from src.arrays.product_except_self.product_calculator import ProductCalculator
from src.arrays.product_except_self.product_calculator_imp import ProductCalculatorImp


@pytest.fixture(params=[
    ProductCalculatorImp
]
)
def product_calculator(request: pytest.FixtureRequest):
    return request.param()


@pytest.mark.parametrize("nums, result", [
    ([1, 2, 3, 4], [24, 12, 8, 6]),
    ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
    ([1, 2, 3, 4], [24, 12, 8, 6]),
    ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0])
])
def test_should_return_array_of_products_except_itself(product_calculator: ProductCalculator,
                                                       nums: List[int], result: List[int]):
    array = [1, 2, 3, 4]
    product_results = product_calculator.product_except_self(array)
    assert product_results == [24, 12, 8, 6]
