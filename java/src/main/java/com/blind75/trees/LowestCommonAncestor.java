package com.blind75.trees;

public class LowestCommonAncestor {
    public TreeNode lowestCommonAncestor(TreeNode treeNode, TreeNode node1, TreeNode node2) {
        TreeNode result = null;
        while (treeNode != null) {
            if (node1.val < treeNode.val && node2.val < treeNode.val) {
                treeNode = treeNode.left;
            } else if (node1.val > treeNode.val && node2.val > treeNode.val) {
                treeNode = treeNode.right;
            } else {
                result = treeNode;
                break;
            }
        }
        return result;
    }
}
