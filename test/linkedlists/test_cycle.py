from src.linkedlists.cycle import Solution
from src.linkedlists.utils import ListNode
from test.linkedlists.utils import array2LinkedList


def testHasCycle1():
    inputList: ListNode = array2LinkedList([3, 2, 0, -4])
    # Make the last node next pointer to the second node
    inputList.next.next.next.next = inputList.next
    listHasCycle = Solution().hasCycle(inputList)
    assert listHasCycle == True


def testHasCycle2():
    inputList: ListNode = array2LinkedList([1, 2])
    # Make the last node next pointer to the first node
    inputList.next.next = inputList
    listHasCycle = Solution().hasCycle(inputList)
    assert listHasCycle == True


def testHasCycle3():
    inputList: ListNode = array2LinkedList([1])
    listHasCycle = Solution().hasCycle(inputList)
    assert listHasCycle == False
