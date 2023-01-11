from src.strings.encode import Solution


def testEncode1():
    inputString = "Hello Jennny"
    compressedString = Solution().compressString(inputString)
    assert compressedString == "Hel2o Jen3y"