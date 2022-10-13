from src.strings.valid_parenthesis import Solution


def testValidParenthesis1():
    inputString = "()"
    areParenthesisValid = Solution().isValid(inputString)
    assert areParenthesisValid == True


def testValidParenthesis2():
    inputString = "()[]{}"
    areParenthesisValid = Solution().isValid(inputString)
    assert areParenthesisValid == True


def testValidParenthesis3():
    inputString = "(]"
    areParenthesisValid = Solution().isValid(inputString)
    assert areParenthesisValid == False


def testValidParenthesis4():
    inputString = ")([]"
    areParenthesisValid = Solution().isValid(inputString)
    assert areParenthesisValid == False
