from src.dynamic_prog.coin_change import Solution


def testCoinChange1():
    coins = [1, 2, 5]
    amount = 11
    minNumCoins = Solution().coinChange(coins, amount)
    assert minNumCoins == 3


def testCoinChange2():
    coins = [2]
    amount = 3
    minNumCoins = Solution().coinChange(coins, amount)
    assert minNumCoins == -1
