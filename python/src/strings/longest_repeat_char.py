from typing import List


class Solution:
    def findMaxLetterInWindow(self, chars: List[str]) -> int:
        letterCounter = {}
        for char in chars:
            if char not in letterCounter:
                letterCounter[char] = 1
            else:
                letterCounter[char] += 1
        return sorted(list(letterCounter.values()))[-1]

    def characterReplacement(self, string: str, target: int) -> int:
        maxRepeatChar = 0
        leftPointer = 0
        rightPointer = 0

        while rightPointer < len(string):
            currentWord = string[leftPointer:rightPointer + 1]
            countDominantChar = self.findMaxLetterInWindow(currentWord)
            while ((rightPointer - leftPointer + 1) - countDominantChar) > target:
                leftPointer += 1
            currentWindow = rightPointer - leftPointer + 1
            maxRepeatChar = max(maxRepeatChar, currentWindow)
            rightPointer += 1
        return maxRepeatChar
