from src.arrays.min_rotated_array import Solution


def testFindMin1():
    array = [3, 4, 5, 1, 2]
    actual_min = Solution().findMin(array)
    expected_min = 1
    assert actual_min == expected_min


def testFindMin2():
    array = [4, 5, 6, 7, 0, 1, 2]
    actual_min = Solution().findMin(array)
    expected_min = 0
    assert actual_min == expected_min


def testFindMin3():
    array = [20, 30, 10, 11, 12]
    actual_min = Solution().findMin(array)
    expected_min = 10
    assert actual_min == expected_min
