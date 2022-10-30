from typing import List

from src.linkedlists.merge_k_lists import Solution
from src.linkedlists.utils import ListNode
from test.linkedlists.utils import array2LinkedList, linkedList2Array


def testMergeKSortedLists():
    lists: List[ListNode] = [array2LinkedList([1, 4, 5]), array2LinkedList([1, 3, 4]), array2LinkedList([2, 6])]
    mergedList = Solution().mergeKLists(lists)
    expectedMergeList = [1, 1, 2, 3, 4, 4, 5, 6]
    assert linkedList2Array(mergedList) == expectedMergeList
