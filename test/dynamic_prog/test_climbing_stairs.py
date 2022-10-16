from src.dynamic_prog.climbing_stairs import Solution


def testClimbingStairs1():
    num_stairs = 2
    num_ways = Solution().climbStairs(num_stairs)
    expected_ways = 2
    assert num_ways == expected_ways


def testClimbingStairs2():
    num_stairs = 3
    num_ways = Solution().climbStairs(num_stairs)
    expected_ways = 3
    assert num_ways == expected_ways
