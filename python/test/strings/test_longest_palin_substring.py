import pytest

from src.strings.longest_palin_substring.palin_substring_finder import LongestPalindromeSubstringFinder
from src.strings.longest_palin_substring.palin_substring_finder_imp import LongestPalindromeSubstringFinderImp


@pytest.fixture(params=[
    LongestPalindromeSubstringFinderImp
])
def palindrome_substring_finder(request: pytest.FixtureRequest):
    return request.param()


@pytest.mark.parametrize("input_string, exp_longest_palindrome", [
    ("babad", "bab"),
    ("cbbd", "bb"),
    ("ac", "a")
])
def test_should_return_the_longest_palindrome_substring(palindrome_substring_finder: LongestPalindromeSubstringFinder,
                                                        input_string: str, exp_longest_palindrome: str):
    assert palindrome_substring_finder.longest_palindrome(input_string) == exp_longest_palindrome
