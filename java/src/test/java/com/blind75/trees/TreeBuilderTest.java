package com.blind75.trees;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import static com.blind75.trees.Utils.buildTreeFromArray;
import static com.blind75.trees.Utils.isTheSameTree;

public class TreeBuilderTest {

    @Test
    public void testBuildTree1() {
        var preOrder = new int[]{3,9,20,15,7};
        var inOrder = new int[]{9,3,15,20,7};
        var builtTree = new TreeBuilder().buildTree(preOrder, inOrder);
        var expectedTree = buildTreeFromArray(new Integer[]{3,9,20,null,null,15,7});
        Assertions.assertTrue(isTheSameTree(builtTree, expectedTree));
    }

    @Test
    public void testBuildTree2() {
        var preOrder = new int[]{-1};
        var inOrder = new int[]{-1};
        var builtTree = new TreeBuilder().buildTree(preOrder, inOrder);
        var expectedTree = buildTreeFromArray(new Integer[]{-1});
        Assertions.assertTrue(isTheSameTree(builtTree, expectedTree));
    }
}
