from src.strings.longest_substring.longest_substr_finder import LongestSubstringFinder


class LongestSubstringFinderImp(LongestSubstringFinder):
    def get_length_of_longest_substring(self, input_string: str) -> int:
        visited: set[str] = set()
        left_pt, result = 0, 0
        for right_pt in range(len(input_string)):
            while input_string[right_pt] in visited:
                visited.remove(input_string[left_pt])
                left_pt += 1
            visited.add(input_string[right_pt])
            result = max(result, (right_pt - left_pt) + 1)
        return result
