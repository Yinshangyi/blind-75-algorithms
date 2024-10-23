from src.linkedlists.reorder_list import Solution
from src.linkedlists.utils import ListNode
from test.linkedlists.utils import array_2_linked_list, linked_list_2_array


def testReOrderList1():
    inputNode: ListNode = array_2_linked_list([1, 2, 3, 4])
    Solution().reorderList(inputNode)
    expectedOutputList = [1, 4, 2, 3]
    assert linked_list_2_array(inputNode) == expectedOutputList


def testReOrderList2():
    inputNode: ListNode = array_2_linked_list([1, 2, 3, 4, 5])
    Solution().reorderList(inputNode)
    expectedOutputList = [1, 5, 2, 4, 3]
    assert linked_list_2_array(inputNode) == expectedOutputList
