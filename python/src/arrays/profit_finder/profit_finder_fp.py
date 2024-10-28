from functools import reduce
from typing import List

from src.arrays.profit_finder.profit_finder import ProfitFinder


class ProfitFinderFP(ProfitFinder):
    def get_max_profit(self, prices: List[int]) -> int:
        def profit_reducer(acc: tuple[int, int], price: int) -> tuple[int, int]:
            min_buy_price, best_profit = acc
            new_min_buy_price = min(min_buy_price, price)
            new_best_profit = max(best_profit, price)
            return new_min_buy_price, new_best_profit

        min_buy_price, best_profit = reduce(profit_reducer, prices, (prices[0], 0))
        return best_profit
