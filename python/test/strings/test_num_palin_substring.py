import pytest

from src.strings.num_palin_substring.palin_substr_finder import PalindromeSubstringFinder
from src.strings.num_palin_substring.palin_substr_finder_fp import PalindromeSubstringFinderFP
from src.strings.num_palin_substring.palin_substr_finder_imp import PalindromeSubstringFinderImp


@pytest.fixture(params=[
    PalindromeSubstringFinderImp,
    PalindromeSubstringFinderFP
])
def substring_finder(request: pytest.FixtureRequest):
    return request.param()


@pytest.mark.parametrize("input_str, exp_num_palindromes", [
    ("abc", 3),
    ("aaa", 6)
])
def test_should_return_the_number_of_palindromes(substring_finder: PalindromeSubstringFinder,
                                                 input_str: str, exp_num_palindromes: str):
    assert substring_finder.count_substrings(input_str) == exp_num_palindromes
