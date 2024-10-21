from typing import List

from src.arrays.profit_finder.profit_finder import ProfitFinder


class ProfitFinderFP(ProfitFinder):
    # [7, 1, 5, 3, 6, 4] --> 5
    def maxProfit(self, prices: List[int]) -> int:
        def