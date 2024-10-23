from typing import Optional

from src.linkedlists.merge_list.list_merger import ListMerger
from src.linkedlists.utils import ListNode


class ListMergerFP(ListMerger):

    def merge_two_lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val <= list2.val:
            return ListNode(list1.val, self.merge_two_lists(list1.next, list2))
        else:
            return ListNode(list2.val, self.merge_two_lists(list1, list2.next))
