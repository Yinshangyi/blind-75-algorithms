from src.trees.k_smallest_item import Solution
from test.trees.utils import buildTree, printTree


def testKthSmallest1():
    treeNode = buildTree([3, 1, 4, None, 2])
    k = 1
    smallestElement = Solution().kthSmallest(treeNode, k)
    assert smallestElement == 1


def testKthSmallest2():
    treeNode = buildTree([5, 3, 6, 2, 4, None, None, 1])
    k = 3
    smallestElement = Solution().kthSmallest(treeNode, k)
    assert smallestElement == 3


def testKthSmallest3():
    treeNode = buildTree([3, 1, 4, None, 2])
    k = 2
    smallestElement = Solution().kthSmallest(treeNode, k)
    assert smallestElement == 2


25


def testKthSmallest4():
    treeNode = buildTree(
        [41, 37, 44, 24, 39, 42, 48, 1, 35, 38, 40, None, 43, 46, 49, 0, 2, 30, 36, None, None, None, None, None, None,
         45, 47, None, None, None, None, None, 4, 29, 32, None, None, None, None, None, None, 3, 9, 26, None, 31, 34,
         None, None, 7, 11, 25, 27, None, None, 33, None, 6, 8, 10, 16, None, None, None, 28, None, None, 5, None, None,
         None, None, None, 15, 19, None, None, None, None, 12, None, 18, 20, None, 13, 17, None, None, 22, None, 14,
         None, None, 21, 23]
        )
    printTree(treeNode)
    k = 25
    smallestElement = Solution().kthSmallest(treeNode, k)
    assert smallestElement == 24


3
