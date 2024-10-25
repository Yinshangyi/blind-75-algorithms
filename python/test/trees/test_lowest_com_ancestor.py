from src.trees.lowest_com_ancestor import Solution
from src.trees.utils import TreeNode
from test.trees.utils import build_tree, printTree


def testLowestCommonAncestor1():
    treeNode = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    node1 = TreeNode(2)
    node2 = TreeNode(8)
    ancestorNode = Solution().lowestCommonAncestor(treeNode, node1, node2)
    assert ancestorNode.val == 6


def testLowestCommonAncestor2():
    treeNode = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    node1 = TreeNode(2)
    node2 = TreeNode(4)
    ancestorNode = Solution().lowestCommonAncestor(treeNode, node1, node2)
    assert ancestorNode.val == 2


def testLowestCommonAncestor3():
    treeNode = build_tree([2, 1])
    node1 = TreeNode(2)
    node2 = TreeNode(1)
    ancestorNode = Solution().lowestCommonAncestor(treeNode, node1, node2)
    assert ancestorNode.val == 2


def testLowestCommonAncestor4():
    treeNode = build_tree([3, 1, 8, None, None, 5, 10, 4, 6, 9, 11])
    printTree(treeNode)
    node1 = TreeNode(9)
    node2 = TreeNode(11)
    ancestorNode = Solution().lowestCommonAncestor(treeNode, node1, node2)
    assert ancestorNode.val == 10
