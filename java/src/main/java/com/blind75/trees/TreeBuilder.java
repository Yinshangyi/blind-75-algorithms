package com.blind75.trees;

import java.util.ArrayList;
import java.util.List;

public class TreeBuilder {

    private List<Integer> buildListFromArray(int[] array) {
        var list = new ArrayList<Integer>();
        for (int item : array) {
            list.add(item);
        }
        return list;
    }

    private TreeNode helper(List<Integer> preOrder, List<Integer> inOrder) {
        if (preOrder.isEmpty() || inOrder.isEmpty()) {
            return null;
        }
        var rootValue = preOrder.get(0);
        var root = new TreeNode(rootValue);
        var midIndex = inOrder.indexOf(rootValue);
        root.left = helper(preOrder.subList(1, midIndex + 1), inOrder.subList(0, midIndex));
        root.right = helper(preOrder.subList(midIndex+1, preOrder.size()), inOrder.subList(midIndex+1, inOrder.size()));
        return root;
    }

    public TreeNode buildTree(int[] preOrder, int[] inOrder) {
        var preOrderItems = buildListFromArray(preOrder);
        var inOrderItems = buildListFromArray(inOrder);
        return helper(preOrderItems, inOrderItems);
    }
}
