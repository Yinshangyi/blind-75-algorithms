package com.blind75.graphs;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class NumberIslandsTest {

    @Test
    public void testGetNumberIslands1() {
        var grid = new char[][]{
                {'1', '1', '1', '1', '0'},
                {'1', '1', '0', '1', '0'},
                {'1', '1', '0', '0', '0'},
                {'0', '0', '0', '0', '0'}
        };
        var numberOfIslands = new NumberIslands().numIslands(grid);
        Assertions.assertEquals(1, numberOfIslands);
    }

    @Test
    public void testGetNumberIslands2() {
        var grid = new char[][]{
                {'1', '1', '0', '0', '0'},
                {'1', '1', '0', '0', '0'},
                {'0', '0', '1', '0', '0'},
                {'0', '0', '0', '1', '1'}
        };
        var numberOfIslands = new NumberIslands().numIslands(grid);
        Assertions.assertEquals(3, numberOfIslands);
    }
}
