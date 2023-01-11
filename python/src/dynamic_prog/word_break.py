from functools import lru_cache
from typing import List


class Solution:
    def wordBreak(self, inputString: str, wordDict: List[str]) -> bool:
        @lru_cache(maxsize=None)
        def checkAllWordsInWordDict(startPointer: int) -> bool:
            if startPointer == len(inputString):
                return True
            for endPointer in range(startPointer + 1, len(inputString) + 1):
                if inputString[startPointer:endPointer] in wordDict and checkAllWordsInWordDict(endPointer):
                    return True
            return False
        return checkAllWordsInWordDict(0)
