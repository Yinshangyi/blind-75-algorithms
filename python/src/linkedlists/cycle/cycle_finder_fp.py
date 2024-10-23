from typing import Optional, Set

from src.linkedlists.cycle.cycle_finder import CycleFinder
from src.linkedlists.utils import ListNode


class CycleFinderFP(CycleFinder):
    def has_cycle(self, head: Optional[ListNode]) -> bool:
        # @formatter: off
        def helper(_head: Optional[ListNode], visited: Set[ListNode]) -> bool:
            match _head:
                case None:
                    return False
                case ListNode(val=_, next=next_node):
                    return True if _head in visited else helper(next_node, visited | {_head})

        return helper(head, set())
