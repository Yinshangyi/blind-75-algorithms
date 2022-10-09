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

    def lengthOfLongestSubstringTwoPointers(self, string: str) -> str:
        rightPointer = 0
        leftPointer = 0
        longestSubstr = 0
        charsCounter = {}

        while rightPointer < len(string):
            charRightPointer = string[rightPointer]
            if charRightPointer not in charsCounter:
                charsCounter[charRightPointer] = 0
            charsCounter[charRightPointer] += 1

            numCharsRepeats = len([char for char in charsCounter.values() if char > 1])
            # If the character is already in the current window
            # Move the left pointer until all characters are unique
            while numCharsRepeats > 0 and leftPointer < rightPointer:
                charLeftPointer = string[leftPointer]
                charsCounter[charLeftPointer] -= 1
                leftPointer += 1
            window = rightPointer - leftPointer + 1
            longestSubstr = max(longestSubstr, window)
            rightPointer += 1
        return longestSubstr
