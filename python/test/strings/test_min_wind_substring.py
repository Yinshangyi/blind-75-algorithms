import pytest

from src.strings.min_wind_substring.min_wind_finder import MinWindSubStringFinder
from src.strings.min_wind_substring.min_wind_finder_imp import MinWindSubStringFinderImp


@pytest.fixture(params=[
    MinWindSubStringFinderImp
])
def substring_finder(request: pytest.FixtureRequest):
    return request.param()


@pytest.mark.parametrize("sub_string1, sub_string2, exp_window", [
    ("ADOBECODEBANC", "ABC", "BANC"),
    ("a", "aa", ""),
    ("AUIABVC", "ABC", "ABVC")
])
def test_should_return_the_minimum_substring_from_substring1_having_all_the_characters_from_substring2(
        substring_finder: MinWindSubStringFinder, sub_string1: str,
        sub_string2: str, exp_window: str):
    assert substring_finder.min_window(sub_string1, sub_string2) == exp_window
