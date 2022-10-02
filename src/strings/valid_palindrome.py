class Solution:
    def isPalindrome(self, string: str) -> bool:
        onlyAphaNum = "".join([char for char in string if char.isalnum()])
        cleanString = onlyAphaNum.lower()
        leftPointer = 0
        rightPointer = len(cleanString) - 1
        while leftPointer < rightPointer:
            if cleanString[leftPointer] != cleanString[rightPointer]:
                return False
            leftPointer += 1
            rightPointer -= 1
        return True
