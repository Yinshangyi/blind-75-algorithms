class Solution:
    def findMaxLetterInWindow(self, letterCount: dict) -> int:
        return max(letterCount.values())

    def characterReplacement(self, s: str, k: int) -> int:
        lettersCount = {}
        maxChars = 0
        leftPointer = 0
        rightPointer = 0

        while rightPointer < len(s):
            currentLetter = s[rightPointer]
            currentWindow = rightPointer - leftPointer + 1

            # updating letter counter
            lettersCount[currentLetter] = lettersCount.get(currentLetter, 0) + 1

            # If enough replacement for the current window
            while (currentWindow - self.findMaxLetterInWindow(lettersCount)) > k:
                # decrease letter count for the current letter
                leftPointerLetter = s[leftPointer]
                lettersCount[leftPointerLetter] -= 1
                leftPointer += 1
                currentWindow = rightPointer - leftPointer + 1

            maxChars = max(maxChars, currentWindow)
            rightPointer += 1
        return maxChars
