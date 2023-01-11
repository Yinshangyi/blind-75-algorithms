from src.trees.max_depth import Solution
from test.trees.utils import buildTree, printTree


def testMaxDepth():
    treeNode = buildTree([3, 9, 20, None, None, 15, 7])
    treeDepth = Solution().maxDepth(treeNode)
    assert treeDepth == 3

