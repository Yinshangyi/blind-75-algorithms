from src.linkedlists.reverse_list import Solution
from src.linkedlists.utils import ListNode
from test.linkedlists.utils import array_2_linked_list, linked_list_2_array


def testReverseLinkedList():
    inputList: ListNode = array_2_linked_list([1, 2, 3, 4, 5])
    reversedList: ListNode = Solution().reverseList(inputList)
    expectedList: ListNode = array_2_linked_list([5, 4, 3, 2, 1])
    assert linked_list_2_array(reversedList) == linked_list_2_array(expectedList)


def testReverseLinkedListRec():
    inputList: ListNode = array_2_linked_list([1, 2, 3, 4, 5])
    reversedList: ListNode = Solution().reverseListRec(inputList)
    expectedList: ListNode = array_2_linked_list([5, 4, 3, 2, 1])
    assert linked_list_2_array(reversedList) == linked_list_2_array(expectedList)
