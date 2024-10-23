from abc import ABC, abstractmethod
from typing import Optional

from src.linkedlists.utils import ListNode


class ListMerger(ABC):

    @abstractmethod
    def merge_two_lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pass
