package com.blind75.linkedlists;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import static com.blind75.linkedlists.Utils.areTwoLinkedListsEqual;
import static com.blind75.linkedlists.Utils.array2LinkedList;

public class RemoveNItemsTest {

    @Test
    public void testNLastElementsFromLinkedList1() {
        var inputList = array2LinkedList(new int[]{1, 2, 3, 4, 5});
        var k = 2;
        var listWithRemovedElements = new RemoveNItems().removeNthFromEnd(inputList, k);
        var expectedList = array2LinkedList(new int[]{1, 2, 3, 5});
        Assertions.assertTrue(areTwoLinkedListsEqual(listWithRemovedElements, expectedList));
    }

    @Test
    public void testNLastElementsFromLinkedList2() {
        var inputList = array2LinkedList(new int[]{1});
        var k = 1;
        var listWithRemovedElements = new RemoveNItems().removeNthFromEnd(inputList, k);
        Assertions.assertNull(listWithRemovedElements);
    }

    @Test
    public void testNLastElementsFromLinkedList3() {
        var inputList = array2LinkedList(new int[]{1, 2});
        var k = 1;
        var listWithRemovedElements = new RemoveNItems().removeNthFromEnd(inputList, k);
        var expectedList = array2LinkedList(new int[]{1});
        Assertions.assertTrue(areTwoLinkedListsEqual(listWithRemovedElements, expectedList));
    }

    @Test
    public void testNLastElementsFromLinkedList4() {
        var inputList = array2LinkedList(new int[]{1, 2});
        var k = 2;
        var listWithRemovedElements = new RemoveNItems().removeNthFromEnd(inputList, k);
        var expectedList = array2LinkedList(new int[]{2});
        Assertions.assertTrue(areTwoLinkedListsEqual(listWithRemovedElements, expectedList));
    }

}
