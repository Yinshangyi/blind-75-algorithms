from src.graphs.num_islands import Solution


def testGetNumberIslands1():
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    numberIslands = Solution().numIslands(grid)
    assert numberIslands == 1


def testGetNumberIslands2():
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    numberIslands = Solution().numIslands(grid)
    assert numberIslands == 3
