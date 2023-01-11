class Solution:
    def hasStringEvenChar(self, string: int) -> bool:
        return (len(string) % 2) == 0

    def longestPalindrome(self, string: str) -> str:
        longestPal = ""
        for charIndex in range(0, len(string)):
            leftPointer = charIndex
            rightPointer = charIndex + 1 if self.hasStringEvenChar(string) else charIndex
            while leftPointer >= 0 and rightPointer < len(string) \
                    and string[leftPointer] == string[rightPointer]:
                windowSize = rightPointer - leftPointer + 1
                if windowSize > len(longestPal):
                    longestPal = string[leftPointer:rightPointer + 1]
                leftPointer -= 1
                rightPointer += 1
        return longestPal
