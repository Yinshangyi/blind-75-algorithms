package com.blind75.trees;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import static com.blind75.trees.Utils.buildTreeFromArray;


public class MaxDepthTest {

    @Test
    public void testMaxDepth() {
        var treeNode = buildTreeFromArray(new Integer[]{3, 9, 20, null, null, 15, 7});
        var treeDepth = new MaxDepth().maxDepth(treeNode);
        Assertions.assertEquals(3, treeDepth);
    }
}
