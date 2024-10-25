from src.trees.level_order_traversal import Solution
from test.trees.utils import build_tree, printTree


def testLevelOrder1():
    treeNode = build_tree([3, 9, 20, None, None, 15, 7])
    levels = Solution().levelOrder(treeNode)
    expectedLevels = [[3], [9, 20], [15, 7]]
    assert levels == expectedLevels


def testLevelOrder2():
    treeNode = build_tree([1])
    levels = Solution().levelOrder(treeNode)
    expectedLevels = [[1]]
    assert levels == expectedLevels
