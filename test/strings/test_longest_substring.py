from src.strings.longest_substring import Solution


def testLengthOfLongestSubstring1():
    inputString = "abcabcbb"
    longestSubString = Solution().lengthOfLongestSubstring(inputString)
    expectedLongestSubString = 3
    assert longestSubString == expectedLongestSubString


def testLengthOfLongestSubstring2():
    inputString = "pwwkew"
    longestSubString = Solution().lengthOfLongestSubstring(inputString)
    expectedLongestSubString = 3
    assert longestSubString == expectedLongestSubString
