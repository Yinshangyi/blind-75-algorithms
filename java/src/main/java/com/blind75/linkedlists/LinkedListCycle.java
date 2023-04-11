package com.blind75.linkedlists;

import java.util.HashSet;

public class LinkedListCycle {
    public boolean hasCycle(ListNode node) {
       var visitedNode = new HashSet<ListNode>();
       while (node != null) {
           if (visitedNode.contains(node)) {
               return true;
           }
           visitedNode.add(node);
           node = node.next;
       }
       return false;
    }
}
