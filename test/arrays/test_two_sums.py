from src.arrays.two_sum import Solution


def testTwoSum():
    array = [2, 7, 11, 15]
    target = 9
    indexes = Solution().twoSum(array, target)
    assert indexes == [0, 1] or indexes == [1, 0]


def testTwoSumWithSortedArray():
    array = [2, 7, 11, 15]
    target = 9
    indexes = Solution().twoSumWithSortedArray(array, target)
    assert indexes == [0, 1] or indexes == [1, 0]

