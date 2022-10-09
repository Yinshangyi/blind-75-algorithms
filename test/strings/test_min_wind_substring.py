import collections

from src.strings.min_wind_substring import Solution


def testDoesContainTarget1():
    currentInput = collections.Counter({'a': 1, 'b': 2})
    targetInput = collections.Counter({'a': 1, 'b': 2})
    containsTarget = Solution().doesContainTarget(currentInput, targetInput)
    assert containsTarget == True


def testDoesContainTarget2():
    currentInput = collections.Counter({'a': 1, 'b': 2})
    targetInput = collections.Counter({'a': 1, 'b': 2, 'c': 1})
    containsTarget = Solution().doesContainTarget(currentInput, targetInput)
    assert containsTarget == False


def testDoesContainTarget3():
    currentInput = collections.Counter({'a': 2, 'b': 2})
    targetInput = collections.Counter({'a': 1, 'b': 2})
    containsTarget = Solution().doesContainTarget(currentInput, targetInput)
    assert containsTarget == True


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


def testMinWindowSubstring3():
    subString1 = "AUIABVC"
    subString2 = "ABC"
    minWindow = Solution().minWindow(subString1, subString2)
    expectedMinWindow = "ABVC"
    assert minWindow == expectedMinWindow
