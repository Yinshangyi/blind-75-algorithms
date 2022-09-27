class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        charsLatestIndexes = {}
        startIndex = 0
        for currentIndex, char in enumerate(s):
            if char in charsLatestIndexes:
                maxLength = max(maxLength, currentIndex - startIndex)
                startIndex = max(startIndex, charsLatestIndexes[char] + 1)
            charsLatestIndexes[char] = currentIndex
        return max(maxLength, len(s) - startIndex)
