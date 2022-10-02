from src.strings.longest_palin_substring import Solution


def testLongestPalindromicSubString1():
    inputString = "babad"
    longestSubstring = Solution().longestPalindrome(inputString)
    expectedLongestSubstring = "bab"
    assert longestSubstring == expectedLongestSubstring


def testLongestPalindromicSubString2():
    inputString = "cbbd"
    longestSubstring = Solution().longestPalindrome(inputString)
    expectedLongestSubstring = "bb"
    assert longestSubstring == expectedLongestSubstring