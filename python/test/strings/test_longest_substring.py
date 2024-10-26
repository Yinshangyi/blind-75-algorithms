import pytest

from src.strings.longest_substring.longest_substr_finder import LongestSubstringFinder
from src.strings.longest_substring.longest_substr_finder_imp import LongestSubstringFinderImp


@pytest.fixture(params=[
    LongestSubstringFinderImp
])
def substring_finder(request: pytest.FixtureRequest):
    return request.param()


@pytest.mark.parametrize("input_string, exp_length", [
    ("abcabcbb", 3),
    ("pwwkew", 3),
    ("bbbbb", 1),
    ("abcabcbb", 3)
])
def test_should_return_the_length_of_the_longest_substring_without_repetition(substring_finder: LongestSubstringFinder,
                                                                              input_string: str, exp_length: int):
    longest_sub_string = substring_finder.get_length_of_longest_substring(input_string)
    assert longest_sub_string == exp_length
