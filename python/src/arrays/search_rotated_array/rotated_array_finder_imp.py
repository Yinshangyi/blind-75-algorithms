from typing import List

from src.arrays.search_rotated_array.rotated_array_finder import RotatedArrayFinder


class RotatedArrayFinderImp(RotatedArrayFinder):
    def search(self, nums: List[int], target: int) -> int:
        left_pt = 0
        right_pt = len(nums) - 1
        while left_pt <= right_pt:
            mid_pt = (left_pt + right_pt) // 2

            if nums[mid_pt] == target:
                return mid_pt

            # if left half is sorted
            if nums[left_pt] <= nums[mid_pt]:
                if nums[left_pt] <= target <= nums[mid_pt]:
                    right_pt = mid_pt - 1
                else:
                    left_pt = mid_pt + 1

            # If the Right Half is Sorted
            else:
                if nums[mid_pt] <= target <= nums[right_pt]:
                    left_pt = mid_pt + 1
                else:
                    right_pt = mid_pt - 1
        return -1
