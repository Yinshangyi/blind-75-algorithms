package com.blind75.trees;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;

public class LevelOrderTraversal {
    public List<List<Integer>> levelOrder(TreeNode treeNode) {
        List<List<Integer>> levels = new ArrayList<>();
        var queue = new ArrayDeque<TreeNode>();
        if (treeNode != null) {
            queue.add(treeNode);
        }

        while (!queue.isEmpty()) {
            List<Integer> level = new ArrayList<>();
            var queueSize = queue.size();
            for (int i = 0; i < queueSize; i++) {
                var node = queue.remove();
                if (node != null) {
                    level.add(node.val);
                }
                if (node.left != null) {
                    queue.add(node.left);
                }
                if (node.right != null) {
                    queue.add(node.right);
                }
            }
            if (!level.isEmpty()) {
                levels.add(level);
            }
        }
        return levels;
    }
}
