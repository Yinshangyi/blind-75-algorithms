from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        result = nums[0]
        leftIndex = 0
        rightIndex = len(nums)-1
        middleIndex = 0

        while leftIndex <= rightIndex:
            if nums[leftIndex] <= nums[rightIndex]:
                return min(nums[leftIndex], result)
                break
            middleIndex = (leftIndex + rightIndex) // 2
            result = min(nums[middleIndex], result)
            if nums[middleIndex] >= nums[leftIndex]:
                leftIndex = middleIndex + 1
            else:
                rightIndex = middleIndex - 1
        return result