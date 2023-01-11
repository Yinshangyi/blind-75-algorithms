from functools import lru_cache


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache(maxsize=None)
        def memo_solve(pointer1: str, pointer2: str) -> int:
            if pointer1 == len(text1) or pointer2 == len(text2):
                return 0
            if text1[pointer1] == text2[pointer2]:
                return 1 + memo_solve(pointer1 + 1, pointer2 + 1)
            else:
                return max(memo_solve(pointer1 + 1, pointer2), memo_solve(pointer1, pointer2+1))

        return memo_solve(0, 0)
