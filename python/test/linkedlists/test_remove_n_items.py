from src.linkedlists.remove_n_items import Solution
from src.linkedlists.utils import ListNode
from test.linkedlists.utils import array_2_linked_list, linked_list_2_array


def testNLastElementsFromLinkedList1():
    inputList: ListNode = array_2_linked_list([1, 2, 3, 4, 5])
    k = 2
    listWithRemovedElements: ListNode = Solution().removeNthFromEnd(inputList, k)
    expectedList = [1, 2, 3, 5]
    assert linked_list_2_array(listWithRemovedElements) == expectedList


def testNLastElementsFromLinkedList2():
    inputList: ListNode = array_2_linked_list([1])
    k = 1
    listWithRemovedElements: ListNode = Solution().removeNthFromEnd(inputList, k)
    expectedList = []
    assert linked_list_2_array(listWithRemovedElements) == expectedList


def testNLastElementsFromLinkedList3():
    inputList: ListNode = array_2_linked_list([1, 2])
    k = 1
    listWithRemovedElements: ListNode = Solution().removeNthFromEnd(inputList, k)
    expectedList = [1]
    assert linked_list_2_array(listWithRemovedElements) == expectedList


def testNLastElementsFromLinkedList4():
    inputList: ListNode = array_2_linked_list([1, 2])
    k = 2
    listWithRemovedElements: ListNode = Solution().removeNthFromEnd(inputList, k)
    expectedList = [2]
    assert linked_list_2_array(listWithRemovedElements) == expectedList
