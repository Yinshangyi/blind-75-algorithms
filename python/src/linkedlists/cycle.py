from typing import Optional

from src.linkedlists.utils import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes = {}
        while head:
            nodes[head] = head
            if head.next in nodes:
                return True
            head = head.next
        return False
