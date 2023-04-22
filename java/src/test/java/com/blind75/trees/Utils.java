package com.blind75.trees;

import java.util.ArrayList;

public class Utils {

    public static TreeNode buildTreeFromArray(Integer[] nodeValues) {
        if (nodeValues.length == 0) {
            return null;
        }
        var nodeValuesList = new ArrayList<Integer>();
        for (var value : nodeValues) {
            nodeValuesList.add(value);
        }
        var rootValue = nodeValuesList.remove(0);
        var treeRoot = new TreeNode(rootValue);

        var queue = new ArrayList<TreeNode>();
        queue.add(treeRoot);

        while (!queue.isEmpty() && !nodeValuesList.isEmpty()) {
            var node = queue.remove(0);

            var newNodeVal = nodeValuesList.remove(0);
            if (newNodeVal != null) {
                node.left = new TreeNode(newNodeVal);
                queue.add(node.left);
            }

            if (queue.isEmpty() || nodeValuesList.isEmpty()) {
                continue;
            }
            newNodeVal = nodeValuesList.remove(0);
            if (newNodeVal != null) {
                node.right = new TreeNode(newNodeVal);
                queue.add(node.right);
            }
        }
        return treeRoot;
    }

    public static boolean isTheSameTree(TreeNode treeNode1, TreeNode treeNode2) {
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
                && isTheSameTree(treeNode1.left, treeNode2.left)
                && isTheSameTree(treeNode1.right, treeNode2.right);
    }

}
