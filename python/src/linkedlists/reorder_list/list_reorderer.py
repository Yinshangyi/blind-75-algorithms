from abc import ABC, abstractmethod
from typing import Optional

from src.linkedlists.utils import ListNode


class ListReOrderer(ABC):

    @abstractmethod
    def reorder_list(self, head: Optional[ListNode]) -> None:
        pass
