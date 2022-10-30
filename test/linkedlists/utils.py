from typing import List

from src.linkedlists.utils import ListNode


def array2LinkedList(array: List[int]) -> ListNode:
    array.reverse()
    node = ListNode(array.pop())
    currentNode = node
    while array:
        nextNode = ListNode(array.pop())
        currentNode.next = nextNode
        currentNode = currentNode.next
    return node


def linkedList2Array(node: ListNode) -> List[int]:
    array = []
    while node:
        array.append(node.val)
        node = node.next
    return array


def areListsEquals(linkedList1: ListNode, linkedList2: ListNode) -> bool:
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
