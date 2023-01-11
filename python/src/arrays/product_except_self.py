from typing import List


class Solution:
    def productExceptSelfOptimized(self, nums: List[int]) -> List[int]:
        arraySize = len(nums)
        result = [1] * arraySize

        prefix = 1
        postfix = 1

        for n in range(arraySize):
            result[n] *= prefix
            result[~n] *= postfix
            prefix *= nums[n]
            postfix *= nums[~n]
        return result

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arraySize = len(nums)
        result = [0] * arraySize

        prefix = 1
        for n in range(arraySize):
            result[n] = prefix
            prefix *= nums[n]

        postfix = 1
        for n in range(arraySize - 1, -1, -1):
            result[n] *= postfix
            postfix *= nums[n]

        return result
