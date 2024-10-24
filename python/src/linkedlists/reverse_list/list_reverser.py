from abc import ABC, abstractmethod
from typing import Optional

from src.linkedlists.utils import ListNode


class ListReverser(ABC):

    @abstractmethod
    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass
