from typing import List

import pytest

from src.arrays.duplicates_missing.duplicate_missing_finder import DuplicateAndMissingFinder
from src.arrays.duplicates_missing.duplicate_missing_finder_imp import DuplicatesAndMissingFinderImp


@pytest.fixture(params=[
    DuplicatesAndMissingFinderImp
]
)
def finder(request: pytest.FixtureRequest):
    return request.param()


@pytest.mark.parametrize("input_array, exp_values", [
    ([1, 2, 3, 4, 4, 6], (4, 5)),
    ([1, 6, 3, 4, 5, 6], (6, 2)),
    ([1, 2, 3, 4, 2, 6], (2, 5))
])
def test_should_return_the_duplicate_and_missing_value(finder: DuplicateAndMissingFinder, input_array: List[int],
                                                       exp_values: tuple[int, int]):
    duplicate, missing = finder.find_duplicate_and_missing_value(input_array)
    assert duplicate == exp_values[0]
    assert missing == exp_values[1]
