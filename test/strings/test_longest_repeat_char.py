from src.strings.longest_repeat_char import Solution


def testFindMaxLetterInWindow():
    letterCountInput = {"a": 2, "b": 5, "c": 1, "d": 2, "e": 5}
    maxLetterCount = Solution().findMaxLetterInWindow(letterCountInput)
    expectedMaxLetterCount = 5
    assert maxLetterCount == expectedMaxLetterCount


def testCharacterReplacement1():
    inputString = "ABAB"
    num_replacements = 2
    longest_substring = Solution().characterReplacement(inputString, num_replacements)
    expected_longest_substring = 4
    assert longest_substring == expected_longest_substring


def testCharacterReplacement2():
    inputString = "AABABBA"
    num_replacements = 1
    longest_substring = Solution().characterReplacement(inputString, num_replacements)
    expected_longest_substring = 4
    assert longest_substring == expected_longest_substring
