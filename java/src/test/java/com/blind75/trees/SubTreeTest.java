package com.blind75.trees;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import static com.blind75.trees.Utils.buildTreeFromArray;

public class SubTreeTest {

    @Test
    public void testIsSubTree1() {
        var treeNode = buildTreeFromArray(new Integer[]{3, 4, 5, 1, 2});
        var smallTreeNode = buildTreeFromArray(new Integer[]{4, 1, 2});
        var isSubTree = new SubTree().isSubtree(treeNode, smallTreeNode);
        Assertions.assertTrue(isSubTree);
    }

    @Test
    public void testIsSubTree2() {
        var treeNode = buildTreeFromArray(new Integer[]{3, 4, 5, 1, 2, null, null, null, null, 0});
        var smallTreeNode = buildTreeFromArray(new Integer[]{4, 1, 2});
        var isSubTree = new SubTree().isSubtree(treeNode, smallTreeNode);
        Assertions.assertFalse(isSubTree);
    }

}
