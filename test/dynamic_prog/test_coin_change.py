from src.dynamic_prog.coin_change import Solution


def testCoinChange1():
    coins = [1, 2, 5]
    target = 11
    numCoins = Solution().coinChange(coins, target)
    expectedNumCoins = 3
    assert numCoins == expectedNumCoins


def testCoinChange2():
    coins = [186, 419, 83, 408]
    target = 6249
    numCoins = Solution().coinChange(coins, target)
    expectedNumCoins = 20
    assert numCoins == expectedNumCoins


def testCannotCoinChange():
    coins = [2]
    target = 3
    numCoins = Solution().coinChange(coins, target)
    expectedNumCoins = -1
    assert numCoins == expectedNumCoins
