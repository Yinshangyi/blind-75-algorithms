from src.arrays.product_except_self import Solution


def testProductExceptSelf1():
    array = [1, 2, 3, 4]
    productResults = Solution().productExceptSelf(array)
    assert productResults == [24, 12, 8, 6]


def testProductExceptSelf2():
    array = [-1, 1, 0, -3, 3]
    productResults = Solution().productExceptSelf(array)
    assert productResults == [0, 0, 9, 0, 0]
