from typing import List

from src.arrays.max_sub_array.max_sub_array import MaxSubArrayCalculator


class MaxSubArrayCalculatorImp(MaxSubArrayCalculator):

    def find_max_sum(self, nums: List[int]) -> int:
        current_sum = 0
        max_sum = nums[0]
        for num in nums:
            if current_sum < 0:
                current_sum = 0
            current_sum += num
            max_sum = max(max_sum, current_sum)
        return max_sum
