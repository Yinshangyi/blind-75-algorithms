from typing import List

from src.arrays.two_sums.two_sums_finder import TwoSumsFinder


class TwoSumsFinderFP(TwoSumsFinder):
    def find_two_sums_indexes(self, nums: List[int], target: int) -> List[int]:
        # @formatter:off
        def helper(n: int, seen: dict[int, int]) -> List[int]:
            if n == len(nums):
                return []
            diff = target - nums[n]
            if diff in seen:
                return [n, seen[diff]]
            return helper(n + 1, {**seen, nums[n]: n})

        return helper(0, {})
