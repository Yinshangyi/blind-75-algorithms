from src.trees.validate_bst import Solution
from test.trees.utils import buildTree


def testIsValidBst1():
    treeNode = buildTree([2, 1, 3])
    validBst = Solution().isValidBST(treeNode)
    assert validBst == True


def testIsValidBst2():
    treeNode = buildTree([5, 1, 4, None, None, 3, 6])
    validBst = Solution().isValidBST(treeNode)
    assert validBst == False
