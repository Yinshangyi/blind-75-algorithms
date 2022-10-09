from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        target = 0
        nums.sort()
        for firstIndex in range(len(nums)):
            if firstIndex > 0 and nums[firstIndex] == nums[firstIndex - 1]:
                continue
            leftPointer = firstIndex + 1
            rightPointer = len(nums) - 1
            while leftPointer < rightPointer:
                current3sum = nums[firstIndex] + nums[leftPointer] + nums[rightPointer]
                if current3sum > target:
                    rightPointer -= 1
                elif current3sum < target:
                    leftPointer += 1
                else:
                    triplets.append([nums[firstIndex], nums[leftPointer], nums[rightPointer]])
                    leftPointer += 1
                    while nums[leftPointer] == nums[leftPointer - 1] and leftPointer < rightPointer:
                        leftPointer += 1
        return triplets
