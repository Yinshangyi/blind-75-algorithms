from typing import List

from src.arrays.binary_searcher.binary_searcher import BinarySearcher


class BinarySearcherImp(BinarySearcher):

    def binarySearch(self, nums: List[int], target: int) -> int:
        left_pointer = 0
        right_pointer = len(nums) - 1
        while left_pointer <= right_pointer:
            middle_pointer = (left_pointer + right_pointer) // 2
            if nums[middle_pointer] == target:
                return middle_pointer
            if target < nums[middle_pointer]:
                right_pointer = middle_pointer - 1
            else:
                left_pointer = middle_pointer + 1
        return -1
