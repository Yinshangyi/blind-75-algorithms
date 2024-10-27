from functools import reduce

from src.strings.num_palin_substring.palin_substr_finder import PalindromeSubstringFinder


class PalindromeSubstringFinderFP(PalindromeSubstringFinder):

    def find_expanded_palindromes_from_indexes(self, string: str, left_pt: int, right_pt: int,
                                               num_palindromes=0) -> int:
        if left_pt >= 0 and right_pt < len(string) and string[left_pt] == string[right_pt]:
            return self.find_expanded_palindromes_from_indexes(string, left_pt - 1, right_pt + 1, num_palindromes + 1)
        return num_palindromes

    def count_substrings(self, string: str) -> int:
        def palindromes_at_index(num_palindromes: int, index: int) -> int:
            single_center = self.find_expanded_palindromes_from_indexes(string, index, index)
            double_center = self.find_expanded_palindromes_from_indexes(string, index, index + 1)
            return num_palindromes + single_center + double_center

        return reduce(palindromes_at_index, range(len(string)), 0)
