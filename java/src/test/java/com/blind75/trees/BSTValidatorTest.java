package com.blind75.trees;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import static com.blind75.trees.Utils.buildTreeFromArray;

public class BSTValidatorTest {

    @Test
    public void testIsValidBst1() {
        var treeNode = buildTreeFromArray(new Integer[]{2, 1, 3});
        var validBst = new BSTValidator().isValidBST(treeNode);
        Assertions.assertTrue(validBst);
    }

    @Test
    void testIsValidBst2() {
        var treeNode = buildTreeFromArray(new Integer[]{5, 1, 4, null, null, 3, 6});
        var validBst = new BSTValidator().isValidBST(treeNode);
        Assertions.assertFalse(validBst);
    }
}
