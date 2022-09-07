from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> int:
        leftIndex = 0
        rightIndex = len(nums) - 1

        while leftIndex <= rightIndex:
            middleIndex = (leftIndex + rightIndex) // 2
            if target == nums[middleIndex]:
                return middleIndex
            # If we are in the left subarray
            if nums[leftIndex] < nums[middleIndex]:
                # Logic to go to the subarray right or left to the middleIndex
                if target > nums[middleIndex] or target < nums[leftIndex]:
                    leftIndex = middleIndex + 1
                else:
                    rightIndex = middleIndex - 1
            # If we are in the right subarray
            else:
                if target < nums[middleIndex] or target > nums[rightIndex]:
                    rightIndex = middleIndex - 1
                else:
                    leftIndex = middleIndex + 1
        return -1
