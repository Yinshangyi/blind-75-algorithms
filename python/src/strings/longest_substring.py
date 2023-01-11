class Solution:
    def lengthOfLongestSubstring(self, inputString: str) -> int:
        maxLength = 0
        startIndex = 0
        seen = {}
        for index, letter in enumerate(inputString):
            if letter in seen:
                maxLength = max(maxLength, index - startIndex)
                startIndex = max(startIndex, seen[letter] + 1)
            seen[letter] = index
        return max(maxLength, len(inputString) - startIndex)
