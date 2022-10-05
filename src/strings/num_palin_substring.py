class Solution:
    def countPalindrome(self, string, leftPointer, rightPointer):
        numPalindrome = 0
        while leftPointer >= 0 and rightPointer < len(string) \
                and string[leftPointer] == string[rightPointer]:
            numPalindrome += 1
            leftPointer -= 1
            rightPointer += 1
        return numPalindrome

    def countSubstrings(self, string: str) -> int:
        numPalindrome = 0
        for index in range(0, len(string)):
            numPalindrome += self.countPalindrome(string, index, index)
            numPalindrome += self.countPalindrome(string, index, index + 1)
        return numPalindrome
