from src.strings.valid_palindrome import Solution


def testIsPalindrome1():
    inputString = "A man, a plan, a canal: Panama"
    isValidPalindrome = Solution().isPalindrome(inputString)
    assert isValidPalindrome == True


def testIsPalindrome2():
    inputString = "race a car"
    isValidPalindrome = Solution().isPalindrome(inputString)
    assert isValidPalindrome == False


def testIsPalindrome3():
    inputString = " "
    isValidPalindrome = Solution().isPalindrome(inputString)
    assert isValidPalindrome == True

