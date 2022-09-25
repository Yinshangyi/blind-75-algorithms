from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for index, first_value in enumerate(nums):
            if index > 0 and first_value == nums[index - 1]:
                continue

            left = index + 1
            right = len(nums) - 1
            while left < right:
                leftValue = nums[left]
                rightValue = nums[right]
                current_sum = first_value + leftValue + rightValue
                if current_sum > 0:
                    right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    result.append([first_value, leftValue, rightValue])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return result
