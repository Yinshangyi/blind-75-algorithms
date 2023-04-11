package com.blind75.trees;

public class MaxDepth {
    public int maxDepth(TreeNode treeNode) {
        if (treeNode == null) {
            return 0;
        }
        return 1 + Math.max(maxDepth(treeNode.left), maxDepth(treeNode.right));
    }
}
