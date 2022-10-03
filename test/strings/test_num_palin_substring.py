from src.strings.num_palin_substring import Solution


def testNumPalindromeSubString1():
    inputString = "abc"
    numSubstrings = Solution().countSubstrings(inputString)
    expectedNumSubstrings = 3
    assert numSubstrings == expectedNumSubstrings


def testNumPalindromeSubString2():
    inputString = "aaa"
    numSubstrings = Solution().countSubstrings(inputString)
    expectedNumSubstrings = 6
    assert numSubstrings == expectedNumSubstrings
