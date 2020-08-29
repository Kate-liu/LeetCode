package BinaryTreeLevelOrderTraversal;//给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
//
// 
//
// 示例： 
//二叉树：[3,9,20,null,null,15,7], 
//
//     3
//   / \
//  9  20
//    /  \
//   15   7
// 
//
// 返回其层次遍历结果： 
//
// [
//  [3],
//  [9,20],
//  [15,7]
//]
// 
// Related Topics 树 广度优先搜索 
// 👍 615 👎 0


//leetcode submit region begin(Prohibit modification and deletion)

import sun.plugin.javascript.navig.Link;

import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode(int x) { val = x; }
 * }
 */

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}

class Solution1 {
    public List<List<Integer>> levelOrder(TreeNode root) {
        // used BFS method

        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        List<List<Integer>> result = new LinkedList<List<Integer>>();

        if (root == null) {
            return result;
        }

        queue.offer(root);  // add root

        while (!queue.isEmpty()) {
            int levelSize = queue.size();

            List<Integer> levelNode = new LinkedList<Integer>();

            for (int i = 0; i < levelSize; i++) {
                TreeNode level = queue.poll();

                levelNode.add(level.val);  // add current level value

                if (level.left != null) {
                    queue.offer(level.left);
                }
                if (level.right != null) {
                    queue.offer(level.right);
                }
            }

            result.add(levelNode);
        }

        return result;
    }
}
//leetcode submit region end(Prohibit modification and deletion)
