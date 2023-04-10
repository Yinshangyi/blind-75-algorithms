package com.blind75.linkedlists;


public class ReverseLinkedList {
    public ListNode reverseList(ListNode node) {
        if (node == null) {
            return node;
        }
        ListNode prevNode = null;
        var currentNode = node;
        while (currentNode != null) {
            var tmpNextNode = currentNode.next;
            currentNode.next = prevNode;
            prevNode = currentNode;
            currentNode = tmpNextNode;
        }
        return prevNode;
    }
}
