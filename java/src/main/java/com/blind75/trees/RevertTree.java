package com.blind75.trees;

public class RevertTree {
    public TreeNode invertTree(TreeNode treeNode) {
        if (treeNode == null) {
            return null;
        }
        var tmpLeft = treeNode.left;
        treeNode.left = treeNode.right;
        treeNode.right = tmpLeft;
        invertTree(treeNode.left);
        invertTree(treeNode.right);
        return treeNode;
    }
}
