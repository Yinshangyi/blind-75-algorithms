from src.trees.same_tree import Solution
from test.trees.utils import buildTree


def testIsSameTree1():
    treeNode1 = buildTree([1, 2, 3])
    treeNode2 = buildTree([1, 2, 3])
    isSameTree = Solution().isSameTree(treeNode1, treeNode2)
    assert isSameTree == True


def testIsSameTree2():
    treeNode1 = buildTree([1, 2])
    treeNode2 = buildTree([1, None, 2])
    isSameTree = Solution().isSameTree(treeNode1, treeNode2)
    assert isSameTree == False
