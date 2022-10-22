from src.dynamic_prog.longest_inc_subseq import Solution


def testLongestIncreasingSubString1():
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    longestIncSubstring = Solution().lengthOfLIS(nums)
    expectedLongestIncSubstring = 4
    assert longestIncSubstring == expectedLongestIncSubstring


def testLongestIncreasingSubString2():
    nums = [0, 1, 0, 3, 2, 3]
    longestIncSubstring = Solution().lengthOfLIS(nums)
    expectedLongestIncSubstring = 4
    assert longestIncSubstring == expectedLongestIncSubstring


def testLongestIncreasingSubString3():
    nums = [7, 7, 7, 7, 7, 7, 7]
    longestIncSubstring = Solution().lengthOfLIS(nums)
    expectedLongestIncSubstring = 4
    assert longestIncSubstring == expectedLongestIncSubstring
