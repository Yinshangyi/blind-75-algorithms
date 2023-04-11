package com.blind75.linkedlists;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import static com.blind75.linkedlists.Utils.areTwoLinkedListsEqual;
import static com.blind75.linkedlists.Utils.array2LinkedList;

public class MergeKLinkedListTest {

    @Test
    public void testMergeKSortedLists1() {
        var lists = new ListNode[]{
                array2LinkedList(new int[]{1, 4, 5}),
                array2LinkedList(new int[]{1, 3, 4}),
                array2LinkedList(new int[]{2, 6})
        };
        var mergedList = new MergeKLinkedList().mergeKLists(lists);
        var expectedMergeList = array2LinkedList(new int[]{1, 1, 2, 3, 4, 4, 5, 6});
        Assertions.assertTrue(areTwoLinkedListsEqual(mergedList, expectedMergeList));
    }

    @Test
    public void testMergeKSortedLists2() {
        var lists = new ListNode[]{};
        var mergedList = new MergeKLinkedList().mergeKLists(lists);
        Assertions.assertNull(mergedList);
    }

    @Test
    public void testMergeKSortedLists3() {
        var lists = new ListNode[]{null};
        var mergedList = new MergeKLinkedList().mergeKLists(lists);
        Assertions.assertNull(mergedList);
    }
}
