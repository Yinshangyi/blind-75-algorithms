from typing import List

import pytest

from src.arrays.contains_duplicates.duplicate_finder import DuplicateFinder
from src.arrays.contains_duplicates.duplicate_finder_fp import DuplicateFinderFP
from src.arrays.contains_duplicates.duplicate_finder_imp import DuplicateFinderImp


@pytest.fixture(params=[
    DuplicateFinderImp,
    DuplicateFinderFP]
)
def duplicate_finder(request: pytest.FixtureRequest):
    return request.param()


@pytest.mark.parametrize("array", [
    [1, 2, 3, 1],
    [1, 2, 1, 1]
])
def test_should_return_true_is_the_array_contains_duplicates(duplicate_finder: DuplicateFinder, array: List[int]):
    has_duplicates = duplicate_finder.contains_duplicate(array)
    assert has_duplicates


def test_should_return_false_when_all_elements_are_unique(duplicate_finder: DuplicateFinder):
    array = [1, 2, 3, 5]
    has_duplicates = duplicate_finder.contains_duplicate(array)
    assert not has_duplicates


def test_should_return_false_if_array_is_empty(duplicate_finder: DuplicateFinder):
    has_duplicates = duplicate_finder.contains_duplicate([])
    assert not has_duplicates
