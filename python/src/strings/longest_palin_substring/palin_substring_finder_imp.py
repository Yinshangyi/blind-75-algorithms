from src.strings.longest_palin_substring.palin_substring_finder import LongestPalindromeSubstringFinder


class LongestPalindromeSubstringFinderImp(LongestPalindromeSubstringFinder):
    def longest_palindrome(self, string: str) -> str:
        max_palindrome = ""
        for char_pt in range(len(string)):
            left_pt, right_pt = char_pt, char_pt
            max_palindrome = self.expand_check_palindrome(left_pt, right_pt, max_palindrome, string)
            left_pt, right_pt = char_pt, char_pt + 1
            max_palindrome = self.expand_check_palindrome(left_pt,  right_pt, max_palindrome, string)
        return max_palindrome

    def expand_check_palindrome(self, left_pt: int, right_pt: int, max_palindrome: str, string: str):
        while left_pt >= 0 and right_pt < len(string) and string[left_pt] == string[right_pt]:
            window = (right_pt - left_pt) + 1
            if window > len(max_palindrome):
                max_palindrome = string[left_pt:right_pt + 1]
            left_pt -= 1
            right_pt += 1
        return max_palindrome
