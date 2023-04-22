package com.blind75.trees;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import java.util.List;

import static com.blind75.trees.Utils.buildTreeFromArray;

public class LevelOrderTraversalTest {

    @Test
    public void testLevelOrder1() {
        var treeNode = buildTreeFromArray(new Integer[]{3, 9, 20, null, null, 15, 7});
        var levels = new LevelOrderTraversal().levelOrder(treeNode);
        var expectedLevels = List.of(List.of(3), List.of(9, 20), List.of(15, 7));
        Assertions.assertEquals(expectedLevels, levels);
    }

    @Test
    public void testLevelOrder2() {
        var treeNode = buildTreeFromArray(new Integer[]{1});
        var levels = new LevelOrderTraversal().levelOrder(treeNode);
        var expectedLevels = List.of(List.of(1));
        Assertions.assertEquals(expectedLevels, levels);
    }
}
