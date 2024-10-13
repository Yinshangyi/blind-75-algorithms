from typing import List

from src.arrays.min_rotated_array.min_rotated_array import MinRotatedArrayFinder


class MinRotatedArrayFinderFP(MinRotatedArrayFinder):

    def find_min(self, nums: List[int]) -> int:
        # @formatter:off
        def helper(_nums: List[int]) -> int:
            mid = len(_nums) // 2
            match _nums:
                case [item]: return item
                case [left, *_, right] if left < right: return left
                case [left, *_, _] if left < _nums[mid]: return helper(_nums[mid + 1:])
                case _: return helper(_nums[:mid + 1])
        return helper(nums)
