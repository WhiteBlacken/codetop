/*
 * @lc app=leetcode.cn id=104 lang=java
 *
 * [104] 二叉树的最大深度
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int maxDepth(TreeNode root) {
        if(root==null)return 0;
        int[] maxdepth = new int[1];
        dfs(root, 1, maxdepth);
        return maxdepth[0];
    
    }
    public void dfs(TreeNode root, int depth, int[] maxdepth){
        if(root==null)return;
        maxdepth[0] = Math.max(maxdepth[0], depth);
        dfs(root.left, depth+1, maxdepth);
        dfs(root.right, depth+1, maxdepth);
    }
}
// @lc code=end

