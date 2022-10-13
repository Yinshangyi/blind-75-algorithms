from src.trees.max_path_sum import Solution
from test.trees.utils import buildTree


def testMaxPathSum1():
    rootNode = buildTree([1, 2, 3])
    bestPath = Solution().maxPathSum(rootNode)
    assert bestPath == 6


def testMaxPathSum2():
    rootNode = buildTree([-10, 9, 20, None, None, 15, 7])
    bestPath = Solution().maxPathSum(rootNode)
    assert bestPath == 42
