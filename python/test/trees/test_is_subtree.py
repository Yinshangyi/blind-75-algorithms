from src.trees.is_subtree import Solution
from test.trees.utils import buildTree


def testIsSubTree1():
    treeNode = buildTree([3, 4, 5, 1, 2])
    smallTreeNode = buildTree([4, 1, 2])
    subTree = Solution().isSubtree(treeNode, smallTreeNode)
    assert subTree == True


def testIsSubTree2():
    treeNode = buildTree([3, 4, 5, 1, 2, None, None, None, None, 0])
    smallTreeNode = buildTree([4, 1, 2])
    subTree = Solution().isSubtree(treeNode, smallTreeNode)
    assert subTree == False
