from typing import List

from src.arrays.max_prod_sub_array.max_prod_finder import MaxProductSubArrayFinder


class MaxProductSubArrayFinderFPRec(MaxProductSubArrayFinder):
    # @formatter:off
    def max_product(self, nums: List[int]):
        def helper(_nums,  max_prod: int, min_prod: int, res: int) -> int:
            match _nums:
                case []: return res
                case [head, *tail]:
                    new_max_prod = max(max_prod * head, min_prod * head, head)
                    new_min_prod = min(max_prod * head, min_prod * head, head)
                    new_res = max(res, new_max_prod)
                    return helper(tail, new_max_prod, new_min_prod, new_res)
        return helper(nums, 1, 1, max(nums))

