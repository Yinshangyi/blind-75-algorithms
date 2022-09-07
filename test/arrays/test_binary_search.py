from src.arrays.binary_search import Solution


def test_binary_search1():
    array = [1, 3, 5, 10, 20, 25, 30]
    foundItemIndex = Solution().binarySearch(array, 3)
    assert foundItemIndex == 1


def test_binary_search2():
    array = [1, 3, 5, 10, 20, 25, 30]
    foundItemIndex = Solution().binarySearch(array, 28)
    assert foundItemIndex == -1


def test_binary_search_rec_1():
    array = [1, 3, 5, 10, 20, 25, 30]
    foundItemIndex = Solution().binarySearchByRecursion(array, 10)
    assert foundItemIndex == 3


def test_binary_search_rec_2():
    array = [1, 3, 5, 10, 20, 25, 30]
    foundItemIndex = Solution().binarySearchByRecursion(array, 15)
    assert foundItemIndex == -1
