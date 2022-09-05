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
