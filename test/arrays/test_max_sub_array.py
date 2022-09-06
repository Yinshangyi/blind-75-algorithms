from src.arrays.max_sub_array import Solution


def testMaxSubArray1():
    array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    max_sum = Solution().maxSubArray(array)
    assert max_sum == 6


def testMaxSubArray2():
    array = [5, 4, -1, 7, 8]
    max_sum = Solution().maxSubArray(array)
    assert max_sum == 23
