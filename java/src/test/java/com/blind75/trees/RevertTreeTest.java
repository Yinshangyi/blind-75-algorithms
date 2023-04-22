package com.blind75.trees;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import static com.blind75.trees.Utils.buildTreeFromArray;
import static com.blind75.trees.Utils.isTheSameTree;

public class RevertTreeTest {

    @Test
    public void testInvertTree1() {
        var treeNode = buildTreeFromArray(new Integer[]{4, 2, 7, 1, 3, 6, 9});
        var invertedTreeNode = new RevertTree().invertTree(treeNode);
        var expectedInvertedTreeNode = buildTreeFromArray((new Integer[]{4, 7, 2, 9, 6, 3, 1}));
        Assertions.assertTrue(isTheSameTree(invertedTreeNode, expectedInvertedTreeNode));
    }

    @Test
    public void testInvertTree2() {
        var treeNode = buildTreeFromArray(new Integer[]{2, 1, 3});
        var invertedTreeNode = new RevertTree().invertTree(treeNode);
        var expectedInvertedTreeNode = buildTreeFromArray((new Integer[]{2, 3, 1}));
        Assertions.assertTrue(isTheSameTree(invertedTreeNode, expectedInvertedTreeNode));
    }
}
