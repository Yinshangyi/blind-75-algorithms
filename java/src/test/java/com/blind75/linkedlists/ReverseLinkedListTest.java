package com.blind75.linkedlists;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.List;

import static com.blind75.linkedlists.Utils.areTwoLinkedListsEqual;
import static com.blind75.linkedlists.Utils.list2LinkedList;

public class ReverseLinkedListTest {

    @Test
    public void testReverseLinkedList1() {
        var inputList = list2LinkedList(new int[]{1, 2, 3, 4, 5});
        var reversedList = new ReverseLinkedList().reverseList(inputList);
        var expectedList = list2LinkedList(new int[]{5, 4, 3, 2, 1});
        Assertions.assertTrue(areTwoLinkedListsEqual(reversedList, expectedList));
    }
}
