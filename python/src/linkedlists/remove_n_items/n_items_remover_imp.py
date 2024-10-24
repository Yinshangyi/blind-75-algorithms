from typing import Optional

from src.linkedlists.remove_n_items.n_items_remover import NItemsRemover
from src.linkedlists.utils import ListNode


class NItemsRemoverImp(NItemsRemover):

    def remove_nth_from_end(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left_pt = dummy
        right_pt = head
        for _ in range(k):
            right_pt = right_pt.next
        while right_pt:
            right_pt = right_pt.next
            left_pt = left_pt.next
        left_pt.next = left_pt.next.next
        return dummy.next

