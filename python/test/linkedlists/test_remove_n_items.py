from src.linkedlists.remove_n_items import Solution
from src.linkedlists.utils import ListNode
from test.linkedlists.utils import array2LinkedList, linkedList2Array


def testNLastElementsFromLinkedList1():
    inputList: ListNode = array2LinkedList([1, 2, 3, 4, 5])
    k = 2
    listWithRemovedElements: ListNode = Solution().removeNthFromEnd(inputList, k)
    expectedList = [1, 2, 3, 5]
    assert linkedList2Array(listWithRemovedElements) == expectedList


def testNLastElementsFromLinkedList2():
    inputList: ListNode = array2LinkedList([1])
    k = 1
    listWithRemovedElements: ListNode = Solution().removeNthFromEnd(inputList, k)
    expectedList = []
    assert linkedList2Array(listWithRemovedElements) == expectedList


def testNLastElementsFromLinkedList3():
    inputList: ListNode = array2LinkedList([1, 2])
    k = 1
    listWithRemovedElements: ListNode = Solution().removeNthFromEnd(inputList, k)
    expectedList = [1]
    assert linkedList2Array(listWithRemovedElements) == expectedList


def testNLastElementsFromLinkedList4():
    inputList: ListNode = array2LinkedList([1, 2])
    k = 2
    listWithRemovedElements: ListNode = Solution().removeNthFromEnd(inputList, k)
    expectedList = [2]
    assert linkedList2Array(listWithRemovedElements) == expectedList
