from src.arrays.best_time_to_buy import Solution


def testBestTimeToBuy1():
    prices = [7, 1, 5, 3, 6, 4]
    bestDayToSell = Solution().maxProfit(prices)
    assert bestDayToSell == 5


def testBestTimeToBuy2():
    prices = [7, 6, 4, 3, 1]
    bestDayToSell = Solution().maxProfit(prices)
    assert bestDayToSell == 0
