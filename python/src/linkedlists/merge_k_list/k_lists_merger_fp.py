from functools import reduce
from typing import List, Optional

from src.linkedlists.merge_k_list.k_lists_merger import KListsMerger
from src.linkedlists.utils import ListNode


class KListsMergerFP(KListsMerger):

    def merge_two_list(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            return ListNode(l1.val, self.merge_two_list(l1.next, l2))
        else:
            return ListNode(l2.val, self.merge_two_list(l1, l2.next))

    def merge_k_lists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        non_empty_lists = [lst for lst in lists if lst]
        if not non_empty_lists:
            return None
        return reduce(self.merge_two_list, non_empty_lists)
