from src.strings.min_wind_substring import Solution


def testMinWindowSubstring1():
    subString1 = "ADOBECODEBANC"
    subString2 = "ABC"
    minWindow = Solution().minWindow(subString1, subString2)
    expectedMinWindow = "BANC"
    assert minWindow == expectedMinWindow


def testMinWindowSubstring2():
    subString1 = "a"
    subString2 = "aa"
    minWindow = Solution().minWindow(subString1, subString2)
    expectedMinWindow = ""
    assert minWindow == expectedMinWindow
