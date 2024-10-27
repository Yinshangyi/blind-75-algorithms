from src.strings.num_palin_substring.palin_substr_finder import PalindromeSubstringFinder


class PalindromeSubstringFinderImp(PalindromeSubstringFinder):

    def find_expanded_palindromes_from_indexes(self, string: str, left_pt: int, right_pt: int):
        num_palindromes = 0
        while left_pt >= 0 and right_pt < len(string):
            if string[left_pt] == string[right_pt]:
                num_palindromes += 1
            left_pt -= 1
            right_pt += 1
        return num_palindromes

    def count_substrings(self, string: str) -> int:
        num_palindromes = 0
        for index in range(len(string)):
            num_palindromes += self.find_expanded_palindromes_from_indexes(string, index, index)
            num_palindromes += self.find_expanded_palindromes_from_indexes(string, index, index + 1)
        return num_palindromes
