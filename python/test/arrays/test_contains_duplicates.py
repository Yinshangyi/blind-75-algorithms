from src.arrays.contains_duplicates import Solution


def testContainsDuplicate1():
    array = [1, 2, 3, 1]
    hasDuplicates = Solution().containsDuplicate(array)
    assert hasDuplicates == True


def testContainsDuplicate2():
    array = [1, 2, 3, 5]
    hasDuplicates = Solution().containsDuplicate(array)
    assert hasDuplicates == False
