from src.arrays.max_product_sub_array import Solution


def testMaxProduct1():
    array = [2, 3, -2, 4]
    max_product = Solution().maxProduct(array)
    assert max_product == 6


def testMaxProduct2():
    array = [-2, 0, -1]
    max_product = Solution().maxProduct(array)
    assert max_product == 0
