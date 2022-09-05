from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        alreadySeenNumbers = {}
        for number in nums:
            if number in alreadySeenNumbers:
                return True
            else:
                alreadySeenNumbers[number] = number
        return False
