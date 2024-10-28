from typing import List

from src.arrays.duplicates_missing.duplicate_missing_finder import DuplicateAndMissingFinder


class DuplicatesAndMissingFinderImp(DuplicateAndMissingFinder):

    def find_duplicate_and_missing_value(self, nums: List[int]) -> tuple[int, int]:
        char_counter = [0] * len(nums)
        for num in nums:
            char_counter[num - 1] += 1
        duplicate, missing = 0, 0
        for n in range(len(char_counter)):
            if char_counter[n] > 1:
                duplicate = n + 1
            if char_counter[n] == 0:
                missing = n + 1
        return duplicate, missing
