from src.arrays.three_sum import Solution


def testThreeSums():
    nums = [-1, 0, 1, 2, -1, -4]
    expectedResult = [[-1, -1, 2], [-1, 0, 1]]
    result = Solution().threeSum(nums)
    assert result == expectedResult


