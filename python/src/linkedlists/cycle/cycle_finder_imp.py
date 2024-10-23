from typing import Optional, Set

from src.linkedlists.cycle.cycle_finder import CycleFinder
from src.linkedlists.utils import ListNode


class CycleFinderImp(CycleFinder):
    def has_cycle(self, head: Optional[ListNode]) -> bool:
        visited: Set[ListNode] = set()
        current_node = head
        while current_node is not None:
            if current_node in visited:
                return True
            visited.add(current_node)
            current_node = current_node.next
        return False