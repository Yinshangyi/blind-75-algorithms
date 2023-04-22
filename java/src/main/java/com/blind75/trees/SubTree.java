package com.blind75.trees;

public class SubTree {
    public boolean isSubtree(TreeNode treeNode, TreeNode smallTreeNode) {
        if (treeNode == null) {
            return false;
        }
        if (smallTreeNode == null) {
            return true;
        }
        var areTreeEqual = checkTreeEquals(treeNode, smallTreeNode);
        if (areTreeEqual) {
            return true;
        }
        return isSubtree(treeNode.left, smallTreeNode) ||
                isSubtree(treeNode.right, smallTreeNode);
    }

    private boolean checkTreeEquals(TreeNode treeNode, TreeNode smallTreeNode) {
        if (treeNode == null && smallTreeNode == null) {
            return true;
        }
        if (treeNode != null && smallTreeNode == null) {
            return false;
        }
        if (treeNode == null && smallTreeNode != null) {
            return false;
        }
        return treeNode.val == smallTreeNode.val &&
                checkTreeEquals(treeNode.left, smallTreeNode.left) &&
                checkTreeEquals(treeNode.right, smallTreeNode.right);
    }
}
