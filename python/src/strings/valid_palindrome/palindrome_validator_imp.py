from src.strings.valid_palindrome.palindrome_validator import PalindromeValidator


class PalindromeValidatorImp(PalindromeValidator):

    def is_palindrome(self, string: str) -> bool:
        clean_string = "".join([char.lower() for char in string if char.isalnum()])
        left_pt, right_pt = 0, len(clean_string) - 1
        while left_pt < right_pt:
            if clean_string[left_pt] != clean_string[right_pt]:
                return False
            left_pt += 1
            right_pt -= 1
        return True
