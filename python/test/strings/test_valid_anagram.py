import pytest

from src.strings.valid_anagram.AnagramValidator import AnagramValidator
from src.strings.valid_anagram.AnagramValidatorImp import AnagramValidatorImp


@pytest.fixture(params=[
    AnagramValidatorImp
])
def validator(request: pytest.FixtureRequest):
    return request.param()


@pytest.mark.parametrize("input1, input2", [
    ("anagram", "nagaram")
])
def test_should_return_true_if_strings_are_anagram(validator: AnagramValidator, input1: str, input2: str):
    assert validator.is_anagram(input1, input2)


@pytest.mark.parametrize("input1, input2", [
    ("rat", "car"),
    ("a", "ab")
])
def test_should_return_false_if_strings_are_not_anagram(validator: AnagramValidator, input1: str, input2: str):
    assert not validator.is_anagram(input1, input2)
