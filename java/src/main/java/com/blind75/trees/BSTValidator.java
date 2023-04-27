package com.blind75.trees;

public class BSTValidator {

    private boolean validateNode(TreeNode treeNode, double minValue, double maxValue) {
        if (treeNode == null) {
            return true;
        }
        var nodeValid = treeNode.val > minValue && treeNode.val < maxValue;
        if (!nodeValid) {
            return false;
        }
        return validateNode(treeNode.left, minValue, treeNode.val) &&
                validateNode(treeNode.right, treeNode.val, maxValue);
    }

    public boolean isValidBST(TreeNode treeNode) {
        var minValue = Double.NEGATIVE_INFINITY;
        var maxValue = Double.POSITIVE_INFINITY;
        return validateNode(treeNode, minValue, maxValue);
    }
}
