from abc import ABC, abstractmethod
from typing import Optional

from src.linkedlists.utils import ListNode


class NItemsRemover(ABC):

    @abstractmethod
    def removeNthFromEnd(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        pass
