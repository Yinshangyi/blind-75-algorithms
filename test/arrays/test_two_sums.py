from src.arrays.two_sum import Solution


def test_two_sum():
    array = [2, 7, 11, 15]
    target = 9
    indexes = Solution().twoSum(array, target)
    assert indexes == [0, 1] or indexes == [1, 0]
