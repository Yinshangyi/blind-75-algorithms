import pytest

from src.strings.valid_palindrome.palindrome_validator import PalindromeValidator
from src.strings.valid_palindrome.palindrome_validator_fp import PalindromeValidatorFP
from src.strings.valid_palindrome.palindrome_validator_imp import PalindromeValidatorImp


@pytest.fixture(params=[
    PalindromeValidatorImp,
    PalindromeValidatorFP
])
def validator(request: pytest.FixtureRequest):
    return request.param()


@pytest.mark.parametrize("input_string", [
    "A man, a plan, a canal: Panama",
    " ",
    "abba",
    "abcba"
])
def test_should_return_true_if_the_string_is_a_valid_palindrome(validator: PalindromeValidator, input_string: str):
    is_valid_palindrome = validator.is_palindrome(input_string)
    assert is_valid_palindrome


@pytest.mark.parametrize("input_string", [
    "race a car"
])
def test_should_return_false_if_the_string_is_not_a_valid_palindrome(validator: PalindromeValidator, input_string: str):
    is_valid_palindrome = validator.is_palindrome(input_string)
    assert not is_valid_palindrome
