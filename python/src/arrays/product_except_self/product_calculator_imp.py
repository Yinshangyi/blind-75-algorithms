from typing import List

from src.arrays.product_except_self.product_calculator import ProductCalculator


class ProductCalculatorImp(ProductCalculator):

    @staticmethod
    def get_prefix_product_array(nums: List[int]) -> List[int]:
        prefix_prod = [1] * len(nums)
        for n in range(1, len(nums)):
            prefix_prod[n] = prefix_prod[n - 1] * nums[n - 1]
        return prefix_prod

    @staticmethod
    def get_suffix_product_array(nums: List[int]) -> List[int]:
        suffix_prod = [1] * len(nums)
        for n in range(len(nums) - 2, -1, -1):
            suffix_prod[n] = suffix_prod[n + 1] * nums[n + 1]
        return suffix_prod

    def product_except_self(self, nums: List[int]) -> List[int]:
        prefix_prod = self.get_prefix_product_array(nums)
        suffix_prod = self.get_suffix_product_array(nums)
        return [prefix_prod[n] * suffix_prod[n] for n in range(len(nums))]
