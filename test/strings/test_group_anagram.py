from src.strings.group_anagram import Solution


def testGroupAnagram1():
    inputStrings = ["eat", "tea", "tan", "ate", "nat", "bat"]
    groups = Solution().groupAnagrams(inputStrings)
    expectedGroups = [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    assert groups == expectedGroups


def testGroupAnagram2():
    inputStrings = [""]
    groups = Solution().groupAnagrams(inputStrings)
    expectedGroups = [[""]]
    assert groups == expectedGroups


def testGroupAnagram3():
    inputStrings = ["a"]
    groups = Solution().groupAnagrams(inputStrings)
    expectedGroups = [["a"]]
    assert groups == expectedGroups
