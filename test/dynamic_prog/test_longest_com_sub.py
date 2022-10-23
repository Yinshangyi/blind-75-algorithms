from src.dynamic_prog.longest_com_sub import Solution


def testLongestCommonSubsequence1():
    text1 = "abcde"
    text2 = "ace"
    longestSubsequence = Solution().longestCommonSubsequence(text1, text2)
    expectedLongestSubsequence = 3
    assert longestSubsequence == expectedLongestSubsequence


def testLongestCommonSubsequence2():
    text1 = "abc"
    text2 = "abc"
    longestSubsequence = Solution().longestCommonSubsequence(text1, text2)
    expectedLongestSubsequence = 3
    assert longestSubsequence == expectedLongestSubsequence


def testLongestCommonSubsequence3():
    text1 = "abc"
    text2 = "def"
    longestSubsequence = Solution().longestCommonSubsequence(text1, text2)
    expectedLongestSubsequence = 0
    assert longestSubsequence == expectedLongestSubsequence
