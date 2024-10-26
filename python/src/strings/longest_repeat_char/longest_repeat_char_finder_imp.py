from collections import Counter

from src.strings.longest_repeat_char.longest_repeat_char_finder import LongestRepeatCharFinder


class LongestRepeatCharFinderImp(LongestRepeatCharFinder):

    def get_max_repetition_dominant_char(self, current_word: str) -> int:
        return max(Counter(current_word).values())

    def is_window_valid(self, string: str, left_pt: int, right_pt: int, target: int) -> bool:
        window = (right_pt - left_pt) + 1
        if window - self.get_max_repetition_dominant_char(string[left_pt:right_pt + 1]) <= target:
            return True
        return False

    def get_longest_character_with_replacement(self, string: str, target: int) -> int:
        max_repeat_char, left_pt, right_pt = 0, 0, 0
        while right_pt < len(string):
            while not self.is_window_valid(string, left_pt, right_pt, target):
                left_pt += 1
            current_word = string[left_pt: right_pt + 1]
            max_repeat_char = max(max_repeat_char, len(current_word))
            right_pt += 1
        return max_repeat_char
