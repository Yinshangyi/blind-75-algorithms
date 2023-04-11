package com.blind75.trees;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import static com.blind75.trees.Utils.buildTreeFromArray;

public class SameTreeTest {

    @Test
    public void testIsSameTree1() {
        var treeNode1 = buildTreeFromArray(new Integer[]{1, 2, 3});
        var treeNode2 = buildTreeFromArray(new Integer[]{1, 2, 3});
        var isSameTree = new SameTree().isSameTree(treeNode1, treeNode2);
        Assertions.assertTrue(isSameTree);
    }

    @Test
    public void testIsSameTree2() {
        var treeNode1 = buildTreeFromArray(new Integer[]{1, 2});
        var treeNode2 = buildTreeFromArray(new Integer[]{1, null, 2});
        var isSameTree = new SameTree().isSameTree(treeNode1, treeNode2);
        Assertions.assertFalse(isSameTree);
    }

}
