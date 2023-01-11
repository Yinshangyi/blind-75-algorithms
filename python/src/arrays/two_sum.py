from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        already_used_number = {}
        for index in range(len(nums)):
            diff = target - nums[index]
            if diff in already_used_number:
                return [index, already_used_number[diff]]
            else:
                already_used_number[nums[index]] = index

    def twoSumWithSortedArray(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        while left < right:
            currentSum = nums[left] + nums[right]
            if currentSum > target:
                right -= 1
            elif currentSum < target:
                left += 1
            else:
                return [left, right]
