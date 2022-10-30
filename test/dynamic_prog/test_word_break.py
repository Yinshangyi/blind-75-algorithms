from src.dynamic_prog.word_break import Solution


def testWordBreak1():
    inputString = "leetcode"
    wordDict = ["leet", "code"]
    isSegmentable = Solution().wordBreak(inputString, wordDict)
    expectedSegmentable = True
    assert isSegmentable == expectedSegmentable


def testWordBreak2():
    inputString = "applepenapple"
    wordDict = ["apple", "pen"]
    isSegmentable = Solution().wordBreak(inputString, wordDict)
    expectedSegmentable = True
    assert isSegmentable == expectedSegmentable


def testWordBreak3():
    inputString = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    isSegmentable = Solution().wordBreak(inputString, wordDict)
    expectedSegmentable = False
    assert isSegmentable == expectedSegmentable
