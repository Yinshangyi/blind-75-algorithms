from typing import Optional

from src.linkedlists.utils import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummyNode = ListNode(None, head)
        leftNode = dummyNode
        rightNode = head
        while k > 0 and rightNode:
            rightNode = rightNode.next
            k -= 1
        while rightNode:
            rightNode = rightNode.next
            leftNode = leftNode.next
        leftNode.next = leftNode.next.next
        return dummyNode.next
