from src.trees.is_subtree import Solution
from test.trees.utils import build_tree


def testIsSubTree1():
    treeNode = build_tree([3, 4, 5, 1, 2])
    smallTreeNode = build_tree([4, 1, 2])
    subTree = Solution().isSubtree(treeNode, smallTreeNode)
    assert subTree == True


def testIsSubTree2():
    treeNode = build_tree([3, 4, 5, 1, 2, None, None, None, None, 0])
    smallTreeNode = build_tree([4, 1, 2])
    subTree = Solution().isSubtree(treeNode, smallTreeNode)
    assert subTree == False
