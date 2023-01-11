from src.strings.valid_anagram import Solution


def testIsAnagram1():
    input1 = "anagram"
    input2 = "nagaram"
    isInput2AnagramOfInput1 = Solution().isAnagram(input1, input2)
    assert isInput2AnagramOfInput1 == True


def testIsAnagram2():
    input1 = "rat"
    input2 = "car"
    isInput2AnagramOfInput1 = Solution().isAnagram(input1, input2)
    assert isInput2AnagramOfInput1 == False
