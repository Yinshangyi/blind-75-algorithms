from typing import List, Optional

from src.linkedlists.utils import ListNode


def array_2_linked_list(array: List[int]) -> Optional[ListNode]:
    if len(array) == 0:
        return None
    array.reverse()
    node = ListNode(array.pop())
    currentNode = node
    while array:
        nextNode = ListNode(array.pop())
        currentNode.next = nextNode
        currentNode = currentNode.next
    return node


def linked_list_2_array(node: ListNode) -> List[int]:
    if node is None:
        return []
    array = []
    while node:
        array.append(node.val)
        node = node.next
    return array


def are_lists_equals(linkedList1: ListNode, linkedList2: ListNode) -> bool:
    currentNode1 = linkedList1
    currentNode2 = linkedList2
    while currentNode1 or currentNode2:
        if currentNode1 is None and currentNode2 is None:
            return True
        if currentNode1 is None or currentNode2 is None:
            return False
        if currentNode1.val != currentNode2.val:
            return False
        currentNode1 = currentNode1.next
        currentNode2 = currentNode2.next
    return True
