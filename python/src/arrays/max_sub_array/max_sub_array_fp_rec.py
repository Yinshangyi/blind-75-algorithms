from typing import List

from src.arrays.max_sub_array.max_sub_array import MaxSubArrayCalculator


class MaxSubArrayCalculatorFPRec(MaxSubArrayCalculator):

    def find_max_sum(self, nums: List[int]) -> int:
        # @formatter:off
        def helper(_nums: List[int], current_sum: int, max_sum: int) -> int:
            match _nums:
                case []: return max_sum
                case [head, *tail]:
                    new_current_sum = current_sum + head if current_sum > 0 else head
                    new_max_sum = max(max_sum, new_current_sum)
                    return helper(tail, new_current_sum, new_max_sum)
        return helper(nums, 0, nums[0])