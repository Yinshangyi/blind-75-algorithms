from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        maxProduct = 1
        minProduct = 1
        for el in nums:
            if el == 0:
                maxProduct = 1
                minProduct = 1
            currentMaxProduct = maxProduct
            maxProduct = max(el * maxProduct, el * minProduct, el)
            minProduct = min(el * currentMaxProduct, el * minProduct, el)
            result = max(maxProduct, result)
        return result


