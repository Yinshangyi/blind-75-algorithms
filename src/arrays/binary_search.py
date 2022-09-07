from typing import List


class Solution:
    def binarySearch(self, nums: List[int], target: int) -> int:
        leftIndex = 0
        rightIndex = len(nums)-1
        while leftIndex <= rightIndex:
            middleIndex = (leftIndex + rightIndex) // 2
            if nums[middleIndex] == target:
                return middleIndex
            if nums[middleIndex] < target:
                leftIndex = middleIndex + 1
            else:
                rightIndex = middleIndex - 1
        return -1

    def binarySearchByRecursion(self, nums: List[int], target: int):
        def binarySearchRec(nums: List[int], target: int, leftIndex: int, rightIndex: int) -> int:
            if leftIndex <= rightIndex:
                middleIndex = (leftIndex + rightIndex) // 2
                if nums[middleIndex] == target:
                    return middleIndex
                if nums[middleIndex] < target:
                    return binarySearchRec(nums=nums, target=target, leftIndex=middleIndex+1, rightIndex=rightIndex)
                else:
                    return binarySearchRec(nums=nums, target=target, leftIndex=leftIndex, rightIndex=rightIndex-1)
            else:
                return -1

        return binarySearchRec(nums, target, leftIndex=0, rightIndex=len(nums)-1)
