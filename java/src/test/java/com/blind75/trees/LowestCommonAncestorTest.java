package com.blind75.trees;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import static com.blind75.trees.Utils.buildTreeFromArray;

public class LowestCommonAncestorTest {
    
    @Test
    public void testLowestCommonAncestor1() {
        var treeNode = buildTreeFromArray(new Integer[]{6, 2, 8, 0, 4, 7, 9, null, null, 3, 5});
        var node1 = new TreeNode(2);
        var node2 = new TreeNode(8);
        var ancestorNode = new LowestCommonAncestor().lowestCommonAncestor(treeNode, node1, node2);
        Assertions.assertEquals(6, ancestorNode.val);
    }

    @Test
    public void testLowestCommonAncestor2() {
        var treeNode = buildTreeFromArray(new Integer[]{6, 2, 8, 0, 4, 7, 9, null, null, 3, 5});
        var node1 = new TreeNode(2);
        var node2 = new TreeNode(4);
        var ancestorNode = new LowestCommonAncestor().lowestCommonAncestor(treeNode, node1, node2);
        Assertions.assertEquals(2, ancestorNode.val);
    }

    @Test
    public void testLowestCommonAncestor3() {
        var treeNode = buildTreeFromArray(new Integer[]{2, 1});
        var node1 = new TreeNode(2);
        var node2 = new TreeNode(1);
        var ancestorNode = new LowestCommonAncestor().lowestCommonAncestor(treeNode, node1, node2);
        Assertions.assertEquals(2, ancestorNode.val);
    }

    @Test
    public void testLowestCommonAncestor4() {
        var treeNode = buildTreeFromArray(new Integer[]{3, 1, 8, null, null, 5, 10, 4, 6, 9, 11});
        var node1 = new TreeNode(9);
        var node2 = new TreeNode(11);
        var ancestorNode = new LowestCommonAncestor().lowestCommonAncestor(treeNode, node1, node2);
        Assertions.assertEquals(10, ancestorNode.val);
    }

}
