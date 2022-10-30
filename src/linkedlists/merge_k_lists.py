from typing import List, Optional

from src.linkedlists.utils import ListNode


class Solution:
    def arrayLists2Array(self, lists):
        nodes = []
        for linkedList in lists:
            currentNode = linkedList
            while currentNode:
                nodes.append(currentNode)
                currentNode = currentNode.next
        return nodes

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = self.arrayLists2Array(lists)
        nodes.sort(key=lambda node: node.val)
        mergedListStartNode = ListNode(None)
        mergedListCurrentNode = mergedListStartNode
        while nodes:
            mergedListCurrentNode.next = nodes.pop(0)
            mergedListCurrentNode = mergedListCurrentNode.next
        return mergedListStartNode.next
