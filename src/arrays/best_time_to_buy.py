from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPointer = 0
        sellPointer = 0
        maxProfit = 0
        while sellPointer < len(prices):
            if prices[buyPointer] < prices[sellPointer]:
                profit = prices[sellPointer] - prices[buyPointer]
                maxProfit = max(maxProfit, profit)
            else:
                buyPointer = sellPointer
            sellPointer += 1
        return maxProfit