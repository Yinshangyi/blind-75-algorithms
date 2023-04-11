package com.blind75.linkedlists;

public class RemoveNItems {
    public ListNode removeNthFromEnd(ListNode node, int k) {
        var dummyNode = new ListNode(0, node);
        var leftNode = dummyNode;
        var rightNode = node;

        while (rightNode != null && k > 0) {
            rightNode = rightNode.next;
            k--;
        }

        while (rightNode != null) {
            rightNode = rightNode.next;
            leftNode = leftNode.next;
        }

        leftNode.next = leftNode.next.next;
        return dummyNode.next;
    }
}
