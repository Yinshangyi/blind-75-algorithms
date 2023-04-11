package com.blind75.linkedlists;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;

public class MergeKLinkedList {

    public ListNode mergeKLists(ListNode[] lists) {
        var nodesList = new ArrayList<Integer>();
        for(var node : lists) {
            while (node != null) {
                nodesList.add(node.val);
                node = node.next;
            }
        }
        nodesList.sort((a, b) -> Integer.compare(a, b));
        var initNode = new ListNode();
        var currentNode = initNode;
        while (!nodesList.isEmpty()) {
            var newVal = nodesList.remove(0);
            currentNode.next = new ListNode(newVal);
            currentNode = currentNode.next;
        }
        return initNode.next;
    }
}
