import math
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf] * (amount + 1)
        dp[0] = 0
        for target in range(1, amount + 1):
            for coin in coins:
                remaining = target - coin
                if remaining >= 0:
                    dp[target] = min(dp[target], 1 + dp[remaining])
        return dp[amount] if dp[amount] != math.inf else -1
