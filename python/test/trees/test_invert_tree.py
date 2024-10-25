from src.trees.invert_tree import Solution
from test.trees.utils import build_tree, isTheSameTree


def testInvertTree1():
    treeNode = build_tree([4, 2, 7, 1, 3, 6, 9])
    invertedTreeNode = Solution().invertTree(treeNode)
    expectedInvertedTreeNode = build_tree([4, 7, 2, 9, 6, 3, 1])
    assert isTheSameTree(invertedTreeNode, expectedInvertedTreeNode) == True


def testInvertTree2():
    treeNode = build_tree([2, 1, 3])
    invertedTreeNode = Solution().invertTree(treeNode)
    expectedInvertedTreeNode = build_tree([2, 3, 1])
    assert isTheSameTree(invertedTreeNode, expectedInvertedTreeNode) == True
