package com.blind75.trees;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Utils {

    public static TreeNode buildTreeFromArray(Integer[] nodeValues) {
        if(nodeValues.length == 0) {
            return null;
        }
        var nodeValuesList = new ArrayList<Integer>();
        for(var value : nodeValues) {
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

    /*
    def buildTree(values: List[int]) -> TreeNode:
    if not values:
        return None

    it = iter(values)
    root = TreeNode(next(it))
    q = [root]
    for node in q:
        val = next(it, None)
        if val is not None:
            node.left = TreeNode(val)
            q.append(node.left)
        val = next(it, None)
        if val is not None:
            node.right = TreeNode(val)
            q.append(node.right)
    return root
     */
}
