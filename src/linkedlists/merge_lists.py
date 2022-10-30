from typing import Optional

from src.linkedlists.utils import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mergedStartNode = ListNode(None)
        currentMergedNode = mergedStartNode
        while list1 and list2:
            if list1.val <= list2.val:
                currentMergedNode.next = list1
                list1 = list1.next
            else:
                currentMergedNode.next = list2
                list2 = list2.next
            currentMergedNode = currentMergedNode.next
        if list1:
            currentMergedNode.next = list1
        else:
            currentMergedNode.next = list2
        return mergedStartNode.next
