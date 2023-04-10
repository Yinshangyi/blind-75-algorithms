package com.blind75.linkedlists;

import java.util.ArrayList;
import java.util.List;

public class Utils {

    public static ArrayList<Integer> array2ArrayList(int[] array) {
        var list = new ArrayList<Integer>();
        for (var element : array) {
            list.add(element);
        }
        return list;
    }

    public static ListNode array2LinkedList(int[] nodesArray) {
        var nodesList = array2ArrayList(nodesArray);
        var node = nodesList.remove(0);
        var firstNode = new ListNode(node, null);
        var currentNode = firstNode;
        while (!nodesList.isEmpty()) {
            var nextValue = nodesList.remove(0);
            var nextNode = new ListNode(nextValue, null);
            currentNode.next = nextNode;
            currentNode = currentNode.next;
        }
        return firstNode;
    }

    public static List<Integer> linkedList2List(ListNode node) {
        var list = new ArrayList<Integer>();
        while (node != null) {
            var value = node.val;
            list.add(value);
            node = node.next;
        }
        return list;
    }

    public static boolean areTwoLinkedListsEqual(ListNode node1, ListNode node2) {
        var list1 = linkedList2List(node1);
        var list2 = linkedList2List(node2);
        return list1.equals(list2);
    }
}
