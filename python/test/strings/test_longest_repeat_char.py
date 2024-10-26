import pytest

from src.strings.longest_repeat_char.longest_repeat_char_finder import LongestRepeatCharFinder
from src.strings.longest_repeat_char.longest_repeat_char_finder_imp import LongestRepeatCharFinderImp


@pytest.fixture(params=[
    LongestRepeatCharFinderImp
])
def longest_char_finder(request: pytest.FixtureRequest):
    return request.param()


@pytest.mark.parametrize("string_input, k, exp_char_count", [
    ("ABAB", 2, 4),
    ("AABABBA", 1, 4),
])
def test_should_return_the_longest_number_of_repeating_character_with_replacement(
        longest_char_finder: LongestRepeatCharFinder, string_input: str, k: int, exp_char_count: int):
    max_char_count = longest_char_finder.get_longest_character_with_replacement(string_input, k)
    assert max_char_count == exp_char_count
