from src.linkedlists.reorder_list import Solution
from src.linkedlists.utils import ListNode
from test.linkedlists.utils import array2LinkedList, linkedList2Array


def testReOrderList1():
    inputNode: ListNode = array2LinkedList([1, 2, 3, 4])
    Solution().reorderList(inputNode)
    expectedOutputList = [1, 4, 2, 3]
    assert linkedList2Array(inputNode) == expectedOutputList


def testReOrderList2():
    inputNode: ListNode = array2LinkedList([1, 2, 3, 4, 5])
    Solution().reorderList(inputNode)
    expectedOutputList = [1, 5, 2, 4, 3]
    assert linkedList2Array(inputNode) == expectedOutputList
