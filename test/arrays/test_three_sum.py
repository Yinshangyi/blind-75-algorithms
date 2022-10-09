from src.arrays.three_sum_again import Solution


def testThreeSums():
    nums = [-1, 0, 1, 2, -1, -4]
    expectedResult = [[-1, -1, 2], [-1, 0, 1]]
    result = Solution().threeSum(nums)
    assert result == expectedResult
    # assert len(result) == 2
    # assert expectedResult[0] in result
    # assert expectedResult[1] in result


def testTwoSums():
    nums = [-1, 0, 1, 2, -2, 10, -3, 3]
    expectedResult = [[-1, 1], [2, -2], [-3, 3]]
    result = Solution().twoSum(nums)
    assert result == expectedResult
