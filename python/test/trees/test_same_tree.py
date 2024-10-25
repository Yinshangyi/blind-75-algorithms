from src.trees.same_tree import Solution
from test.trees.utils import build_tree


def testIsSameTree1():
    treeNode1 = build_tree([1, 2, 3])
    treeNode2 = build_tree([1, 2, 3])
    isSameTree = Solution().isSameTree(treeNode1, treeNode2)
    assert isSameTree == True


def testIsSameTree2():
    treeNode1 = build_tree([1, 2])
    treeNode2 = build_tree([1, None, 2])
    isSameTree = Solution().isSameTree(treeNode1, treeNode2)
    assert isSameTree == False
