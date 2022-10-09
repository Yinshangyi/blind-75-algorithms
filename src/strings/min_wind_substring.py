from collections import Counter


class Solution:

    def doesContainTarget(self, charCounter: Counter, target: Counter):
        return charCounter & target == target

    def minWindow(self, searchString: str, target: str) -> str:
        minWindowSubstring = ""
        charCounter = Counter()
        targetCounter = Counter(target)
        leftPointer = 0
        rightPointer = 0

        while rightPointer < len(searchString):
            latestChar = searchString[rightPointer]
            charCounter[latestChar] += 1
            while self.doesContainTarget(charCounter, targetCounter):
                window = rightPointer - leftPointer + 1
                firstChar = searchString[leftPointer]
                if window < len(minWindowSubstring) or minWindowSubstring == "":
                    minWindowSubstring = searchString[leftPointer: rightPointer + 1]
                charCounter[firstChar] -= 1
                leftPointer += 1
            rightPointer += 1
        return minWindowSubstring
