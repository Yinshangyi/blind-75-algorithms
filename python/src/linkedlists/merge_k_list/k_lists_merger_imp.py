from typing import List, Optional

from src.linkedlists.merge_k_list.k_lists_merger import KListsMerger
from src.linkedlists.utils import ListNode


class KListsMergerImp(KListsMerger):

    def merge_two_lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode()
        current_node = dummy_node

        while list1 and list2:
            if list1.val <= list2.val:
                current_node.next = list1
                list1 = list1.next
            else:
                current_node.next = list2
                list2 = list2.next
            current_node = current_node.next
        if not list1:
            current_node.next = list2
        else:
            current_node.next = list1
        return dummy_node.next

    def merge_k_lists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        non_empty_lists = [lst for lst in lists if lst]
        if not non_empty_lists:
            return None
        while len(lists) >= 2:
            list1 = lists.pop(0)
            list2 = lists.pop(0)
            merged_list = self.merge_two_lists(list1, list2)
            lists.append(merged_list)
        return lists[0]
