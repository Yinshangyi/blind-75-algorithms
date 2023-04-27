package com.blind75.trees;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import static com.blind75.trees.Utils.buildTreeFromArray;

public class KthSmallestInBSTTest {

    @Test
    public void testKthSmallest1() {
        var treeNode = buildTreeFromArray(new Integer[]{3, 1, 4, null, 2});
        var k = 1;
        var smallestElement = new KthSmallestInBST().kthSmallest(treeNode, k);
        Assertions.assertEquals(1, smallestElement);
    }

    @Test
    public void testKthSmallest2() {
        var treeNode = buildTreeFromArray(new Integer[]{5, 3, 6, 2, 4, null, null, 1});
        var k = 3;
        var smallestElement = new KthSmallestInBST().kthSmallest(treeNode, k);
        Assertions.assertEquals(3, smallestElement);
    }

    @Test
    public void testKthSmallest3() {
        var treeNode = buildTreeFromArray(new Integer[]{3, 1, 4, null, 2});
        var k = 2;
        var smallestElement = new KthSmallestInBST().kthSmallest(treeNode, k);
        Assertions.assertEquals(2, smallestElement);
    }

}
