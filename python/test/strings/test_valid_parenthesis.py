import pytest

from src.strings.valid_parenthesis.parenthesis_validator import ParenthesisValidator
from src.strings.valid_parenthesis.parenthesis_validator_fp import ParenthesisValidatorFP
from src.strings.valid_parenthesis.parenthesis_validator_imp import ParenthesisValidatorImp


@pytest.fixture(params=[
    ParenthesisValidatorImp,
    ParenthesisValidatorFP
])
def validator(request: pytest.FixtureRequest):
    return request.param()


@pytest.mark.parametrize("input_string", [
    "()",
    "()[]{}",
])
def test_should_return_true_if_parenthesis_are_valid(validator: ParenthesisValidator, input_string: str):
    assert validator.is_valid(input_string)


@pytest.mark.parametrize("input_string", [
    "(]"
    ")([]"
])
def test_should_return_false_if_parenthesis_are_not_valid(validator: ParenthesisValidator, input_string: str):
    assert not validator.is_valid(input_string)
