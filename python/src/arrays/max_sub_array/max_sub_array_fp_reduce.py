from functools import reduce
from typing import List

from src.arrays.max_sub_array.max_sub_array import MaxSubArrayCalculator


class MaxSubArrayCalculatorFPReduce(MaxSubArrayCalculator):

    def find_max_sum(self, nums: List[int]) -> int:
        def finder(acc: tuple[int, int], num: int) -> tuple[int, int]:
            current_sum, max_sum = acc
            new_current_sum = current_sum + num if current_sum > 0 else num
            new_max_sum = max(max_sum, new_current_sum)
            return new_current_sum, new_max_sum

        _, max_sum = reduce(finder, nums, (0, nums[0]))
        return max_sum
