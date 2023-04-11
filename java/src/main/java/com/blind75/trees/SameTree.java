package com.blind75.trees;

public class SameTree {
    public boolean isSameTree(TreeNode treeNode1, TreeNode treeNode2) {
        if (treeNode1 == null && treeNode2 != null) {
            return false;
        }
        if (treeNode1 != null && treeNode2 == null) {
            return false;
        }
        if (treeNode1 == null && treeNode2 == null) {
            return true;
        }
        return treeNode1.val == treeNode2.val
                && isSameTree(treeNode1.left, treeNode2.left)
                && isSameTree(treeNode1.right, treeNode2.right);
    }
}
