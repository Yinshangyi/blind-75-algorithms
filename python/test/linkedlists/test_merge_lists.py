from xml.dom.minicompat import NodeList

from src.linkedlists.merge_lists import Solution
from test.linkedlists.utils import array2LinkedList, linkedList2Array


def testMergeLinkedList1():
    list1: NodeList = array2LinkedList([1, 2, 4])
    list2: NodeList = array2LinkedList([1, 3, 4])
    mergedList = Solution().mergeTwoLists(list1, list2)
    expectedMergedList = [1, 1, 2, 3, 4, 4]
    assert linkedList2Array(mergedList) == expectedMergedList
