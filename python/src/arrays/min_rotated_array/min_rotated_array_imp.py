from typing import List

from src.arrays.min_rotated_array.min_rotated_array import MinRotatedArrayFinder


class MinRotatedArrayFinderImp(MinRotatedArrayFinder):
    def find_min(self, nums: List[int]) -> int:
        leftPointer = 0
        rightPointer = len(nums) - 1
        while leftPointer <= rightPointer:
            if nums[leftPointer] <= nums[rightPointer]:
                break
            middlePointer = int((leftPointer + rightPointer) / 2)
            if nums[middlePointer] >= nums[leftPointer]:
                leftPointer = middlePointer + 1
            else:
                rightPointer = middlePointer
        return nums[leftPointer]



