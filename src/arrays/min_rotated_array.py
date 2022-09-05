from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        result = nums[0]
        left = 0
        right = len(nums)-1

        while left <= right:
            if nums[left] < nums[right]:
                result = min(nums[left], result)
                break
            middle = (left + right) // 2
            result = min(result, nums[middle])
            if nums[middle] >= nums[left]:
                left = middle + 1
            else:
                right = middle - 1
        return result