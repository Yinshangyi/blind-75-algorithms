package com.blind75.linkedlists;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import static com.blind75.linkedlists.Utils.areTwoLinkedListsEqual;
import static com.blind75.linkedlists.Utils.array2LinkedList;

public class MergeLinkedListTest {

    @Test
    public void testMergeLinkedList() {
        var list1 = array2LinkedList(new int[]{1, 2, 4});
        var list2 = array2LinkedList(new int[]{1, 3, 4});
        var mergedList = new MergeLinkedList().mergeTwoLists(list1, list2);
        var expectedMergedList = array2LinkedList(new int[]{1, 1, 2, 3, 4, 4});
        Assertions.assertTrue(areTwoLinkedListsEqual(mergedList, expectedMergedList));
    }
}
