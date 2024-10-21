from typing import List

from src.arrays.two_sums.two_sums_finder import TwoSumsFinder


class TwoSumsFinderImp(TwoSumsFinder):

    def find_two_sums_indexes(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for n in range(len(nums)):
            diff = target - nums[n]
            if diff in seen:
                return [n, seen[diff]]
            seen[nums[n]] = n
        return []