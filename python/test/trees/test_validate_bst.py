from src.trees.validate_bst import Solution
from test.trees.utils import build_tree


def testIsValidBst1():
    treeNode = build_tree([2, 1, 3])
    validBst = Solution().isValidBST(treeNode)
    assert validBst == True


def testIsValidBst2():
    treeNode = build_tree([5, 1, 4, None, None, 3, 6])
    validBst = Solution().isValidBST(treeNode)
    assert validBst == False
