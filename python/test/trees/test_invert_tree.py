from src.trees.invert_tree import Solution
from test.trees.utils import buildTree, isTheSameTree


def testInvertTree1():
    treeNode = buildTree([4, 2, 7, 1, 3, 6, 9])
    invertedTreeNode = Solution().invertTree(treeNode)
    expectedInvertedTreeNode = buildTree([4, 7, 2, 9, 6, 3, 1])
    assert isTheSameTree(invertedTreeNode, expectedInvertedTreeNode) == True


def testInvertTree2():
    treeNode = buildTree([2, 1, 3])
    invertedTreeNode = Solution().invertTree(treeNode)
    expectedInvertedTreeNode = buildTree([2, 3, 1])
    assert isTheSameTree(invertedTreeNode, expectedInvertedTreeNode) == True
