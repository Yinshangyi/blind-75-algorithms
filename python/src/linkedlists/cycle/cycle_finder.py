from abc import ABC, abstractmethod
from typing import Optional

from src.linkedlists.utils import ListNode


class CycleFinder(ABC):

    @abstractmethod
    def has_cycle(self, head: Optional[ListNode]) -> bool:
        pass