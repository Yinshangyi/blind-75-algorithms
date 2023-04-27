package com.blind75.trees;

import java.util.ArrayList;
import java.util.List;

public class KthSmallestInBST {

    private void inOrderTraversal(TreeNode treeNode, List<Integer> inOrderList) {
        if (treeNode == null) {
            return;
        }
        inOrderTraversal(treeNode.left, inOrderList);
        inOrderList.add(treeNode.val);
        inOrderTraversal(treeNode.right, inOrderList);
    }
    public int kthSmallest(TreeNode treeNode, int k) {
        var inOrderList = new ArrayList<Integer>();
        inOrderTraversal(treeNode, inOrderList);
        var kSmallestItem = 0;
        while(k > 0) {
            kSmallestItem = inOrderList.remove(0);
            k--;
        }
        return kSmallestItem;
    }
}
