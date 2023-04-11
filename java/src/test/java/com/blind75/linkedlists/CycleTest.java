package com.blind75.linkedlists;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import static com.blind75.linkedlists.Utils.array2LinkedList;

public class CycleTest {
    @Test
    public void testHasCycle1() {
        var inputList = array2LinkedList(new int[]{3, 2, 0, -4});
        // Make the last node next pointer to the second node
        inputList.next.next.next.next = inputList.next;
        var listHasCycle = new LinkedListCycle().hasCycle(inputList);
        Assertions.assertTrue(listHasCycle);
    }

    @Test
    public void testHasCycle2() {
        var inputList = array2LinkedList(new int[]{1, 2});
        inputList.next.next = inputList;
        var listHasCycle = new LinkedListCycle().hasCycle(inputList);
        Assertions.assertTrue(listHasCycle);
    }

    @Test
    public void testHasCycle3() {
        var inputList = array2LinkedList(new int[]{1});
        var listHasCycle = new LinkedListCycle().hasCycle(inputList);
        Assertions.assertFalse(listHasCycle);
    }
}
