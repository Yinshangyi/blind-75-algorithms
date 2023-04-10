package com.blind75.linkedlists;

public class MergeLinkedList {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        var initNode = new ListNode();
        ListNode sortedNode = initNode;

        while (list1 != null || list2 != null) {

            if (list1 == null) {
                sortedNode.next = list2;
                break;
            }

            if (list2 == null) {
                sortedNode.next = list1;
                break;
            }

            if (list1.val <= list2.val) {
                sortedNode.next = list1;
                sortedNode = sortedNode.next;
                list1 = list1.next;
            } else {
                sortedNode.next = list2;
                sortedNode = sortedNode.next;
                list2 = list2.next;
            }
        }
        return initNode.next;
    }
}
