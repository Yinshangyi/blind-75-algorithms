from functools import reduce
from typing import List

from src.arrays.max_prod_sub_array.max_prod_finder import MaxProductSubArrayFinder


class MaxProductSubArrayFinderFPReduce(MaxProductSubArrayFinder):
    # @formatter:off
    def max_product(self, nums: List[int]):
        _, _, result = reduce(self.get_new_values, nums, (1, 1, max(nums)))
        return result

    @staticmethod
    def get_new_values(acc: tuple[int, int, int], num: int) -> tuple[int, int, int]:
        max_prod, min_prod, result = acc
        new_max_prod = max(max_prod * num, min_prod * num, num)
        new_min_prod = min(max_prod * num, min_prod * num, num)
        new_result = max(result, new_max_prod)
        return new_max_prod, new_min_prod, new_result

