from src.arrays.min_rotated_array import Solution


def testFindMin():
    array = [3, 4, 5, 1, 2]
    actual_min = Solution().findMin(array)
    expected_min = 1
    assert actual_min == expected_min