from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
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
