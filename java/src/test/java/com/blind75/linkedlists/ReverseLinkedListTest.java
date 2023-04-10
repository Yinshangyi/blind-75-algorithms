package com.blind75.linkedlists;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import static com.blind75.linkedlists.Utils.areTwoLinkedListsEqual;
import static com.blind75.linkedlists.Utils.array2LinkedList;

public class ReverseLinkedListTest {

    @Test
    public void testReverseLinkedList1() {
        var inputList = array2LinkedList(new int[]{1, 2, 3, 4, 5});
        var reversedList = new ReverseLinkedList().reverseList(inputList);
        var expectedList = array2LinkedList(new int[]{5, 4, 3, 2, 1});
        Assertions.assertTrue(areTwoLinkedListsEqual(reversedList, expectedList));
    }
}
