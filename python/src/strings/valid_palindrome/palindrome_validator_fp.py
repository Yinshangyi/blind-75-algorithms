from typing import List

from src.strings.valid_palindrome.palindrome_validator import PalindromeValidator


class PalindromeValidatorFP(PalindromeValidator):

    def is_palindrome(self, string: str) -> bool:
        # @formatter:off
        def helper(substring: List[str]) -> bool:
            match substring:
                case []: return True
                case [_]: return True
                case [head, *_, tail]:
                    return False if head != tail else helper(substring[1:-1])

        clean_string = [char.lower() for char in string if char.isalnum()]
        return helper(clean_string)
