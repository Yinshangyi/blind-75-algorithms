from typing import List

from src.arrays.binary_searcher.binary_searcher import BinarySearcher


class BinarySearcherFP(BinarySearcher):

    # @formatter:off
    def binarySearch(self, nums: List[int], target: int) -> int:
        def helper(_nums: List[int], left_pt: int, right_pt: int) -> int:
            if left_pt > right_pt:
                return -1
            mid_pt = (left_pt + right_pt) // 2
            if nums[mid_pt] == target:
                return mid_pt
            if target > nums[mid_pt]:
                return helper(nums, mid_pt + 1, right_pt)
            else:
                return helper(nums, left_pt, mid_pt - 1)
        return helper(nums, 0, len(nums) - 1)

