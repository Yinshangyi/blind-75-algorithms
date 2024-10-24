from abc import ABC, abstractmethod
from typing import List, Optional

from src.linkedlists.utils import ListNode


class KListsMerger(ABC):

    @abstractmethod
    def merge_k_lists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pass
