from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = 0
        for el in nums:
            if current_sum < 0:
                current_sum = 0
            current_sum += el
            max_sum = max(current_sum, max_sum)
        return max_sum
