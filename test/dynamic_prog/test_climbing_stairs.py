from src.dynamic_prog.climbing_stairs import Solution


def test_climbing_stairs():
    num_stairs = 2
    num_ways = Solution().climbStairs(num_stairs)
    expected_ways = 2
    assert num_ways == expected_ways
