from src.arrays.search_rotated_array import Solution


def test_search_1():
    array = [4, 5, 6, 7, 0, 1, 2]
    foundItem = Solution().search(array, 0)
    assert foundItem == 4


def test_search_2():
    array = [4, 5, 6, 7, 0, 1, 2]
    foundItem = Solution().search(array, 3)
    assert foundItem == -1


def test_search_3():
    array = [4, 5, 6, 7, 0, 1, 2]
    foundItem = Solution().search(array, 5)
    assert foundItem == 1
