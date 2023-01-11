from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for currentIndex in range(1, len(nums)):
            for previousIndex in range(currentIndex):
                if nums[currentIndex] > nums[previousIndex]:
                    dp[currentIndex] = max(dp[currentIndex], dp[previousIndex] + 1)
        return max(dp)
