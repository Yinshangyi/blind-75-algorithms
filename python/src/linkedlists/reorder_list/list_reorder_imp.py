from typing import Optional

from src.linkedlists.reorder_list.list_reorderer import ListReOrderer
from src.linkedlists.utils import ListNode


class ListReOrdererImp(ListReOrderer):

    def reorder_list(self, head: Optional[ListNode]) -> None:
        currentNode = head
        listArray = []
        while currentNode:
            listArray.append(currentNode)
            currentNode = currentNode.next

        head = listArray.pop(0)
        currentNode = head
        leftPointer = 0
        rightPointer = len(listArray) - 1
        while leftPointer <= rightPointer:
            leftNode = listArray[leftPointer]
            rightNode = listArray[rightPointer]
            currentNode.next = rightNode
            rightNode.next = leftNode
            currentNode = leftNode
            leftPointer += 1
            rightPointer -= 1
        currentNode.next = None
