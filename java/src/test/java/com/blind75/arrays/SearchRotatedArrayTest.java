package com.blind75.arrays;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class SearchRotatedArrayTest {
    @Test
    public void testSearch1() {
        var array = new int[]{4, 5, 6, 7, 0, 1, 2};
        var foundItem = new SearchRotatedArray().search(array, 0);
        Assertions.assertEquals(4, foundItem);
    }

    @Test
    public void testSearch2() {
        var array = new int[]{4, 5, 6, 7, 0, 1, 2};
        var foundItem = new SearchRotatedArray().search(array, 3);
        Assertions.assertEquals(-1, foundItem);
    }

    @Test
    public void testSearch3() {
        var array = new int[]{4, 5, 6, 7, 0, 1, 2};
        var foundItem = new SearchRotatedArray().search(array, 5);
        Assertions.assertEquals(1, foundItem);
    }

}
