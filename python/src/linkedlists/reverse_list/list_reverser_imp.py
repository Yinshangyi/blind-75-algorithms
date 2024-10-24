from typing import Optional

from src.linkedlists.reverse_list.list_reverser import ListReverser
from src.linkedlists.utils import ListNode


class ListReverserImp(ListReverser):

    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
