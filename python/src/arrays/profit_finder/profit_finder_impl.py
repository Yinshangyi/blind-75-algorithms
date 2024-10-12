from typing import List

from src.arrays.profit_finder.profit_finder import ProfitFinder


class ProfitFinderImpl(ProfitFinder):

    def maxProfit(self, prices: List[int]) -> int:
        buy_pointer = 0
        sell_pointer = 0
        max_profit = 0
        while sell_pointer < len(prices):
            if prices[buy_pointer] < prices[sell_pointer]:
                profit = prices[sell_pointer] - prices[buy_pointer]
                max_profit = max(max_profit, profit)
            else:
                buy_pointer = sell_pointer
            sell_pointer += 1
        return max_profit
