from typing import List

from src.linkedlists.merge_k_lists import Solution
from src.linkedlists.utils import ListNode
from test.linkedlists.utils import array_2_linked_list, linked_list_2_array


def testMergeKSortedLists():
    lists: List[ListNode] = [array_2_linked_list([1, 4, 5]), array_2_linked_list([1, 3, 4]), array_2_linked_list([2, 6])]
    mergedList = Solution().mergeKLists(lists)
    expectedMergeList = [1, 1, 2, 3, 4, 4, 5, 6]
    assert linked_list_2_array(mergedList) == expectedMergeList
