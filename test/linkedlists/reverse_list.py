from src.linkedlists.reverse_list import Solution
from src.linkedlists.utils import ListNode
from test.linkedlists.utils import array2LinkedList, linkedList2Array


def testReverseLinkedList():
    inputList: ListNode = array2LinkedList([1, 2, 3, 4, 5])
    reversedList: ListNode = Solution().reverseList(inputList)
    expectedList: ListNode = array2LinkedList([5, 4, 3, 2, 1])
    assert linkedList2Array(reversedList) == linkedList2Array(expectedList)


def testReverseLinkedListRec():
    inputList: ListNode = array2LinkedList([1, 2, 3, 4, 5])
    reversedList: ListNode = Solution().reverseListRec(inputList)
    expectedList: ListNode = array2LinkedList([5, 4, 3, 2, 1])
    assert linkedList2Array(reversedList) == linkedList2Array(expectedList)
