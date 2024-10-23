from typing import Optional

from src.linkedlists.merge_list.list_merger import ListMerger
from src.linkedlists.utils import ListNode


class ListMergerImp(ListMerger):

    def merge_two_lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(None)
        current = dummy_node
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        if list1 and not list2:
            current.next = list1
        elif list2 and not list1:
            current.next = list2
        return dummy_node.next
