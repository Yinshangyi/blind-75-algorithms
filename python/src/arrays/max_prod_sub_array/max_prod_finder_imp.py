from typing import List

from src.arrays.max_prod_sub_array.max_prod_finder import MaxProductSubArrayFinder


class MaxProductSubArrayFinderImp(MaxProductSubArrayFinder):

    def max_product(self, nums: List[int]):
        result = max(nums)
        min_prod, max_prod = 1, 1
        for item in nums:
            tmp_max_prod = max_prod
            max_prod = max(max_prod * item, min_prod * item, item)
            min_prod = min(tmp_max_prod * item, min_prod * item, item)
            result = max(result, max_prod)
        return result
