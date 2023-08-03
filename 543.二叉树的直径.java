/*
 * @lc app=leetcode.cn id=543 lang=java
 *
 * [543] 二叉树的直径
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
    public int diameterOfBinaryTree(TreeNode root) {
        //转换成对某个子树求最大直径
        int[] diameter = new int[1];
        maxDiameter(root, diameter);
        return diameter[0];
    }

    public int maxDiameter(TreeNode root, int[] diameter){
        if(root==null) return -1;
        int leftDiameter = maxDiameter(root.left, diameter);
        int rightDiameter = maxDiameter(root.right, diameter);
        diameter[0] = Math.max(diameter[0], leftDiameter + rightDiameter + 2);
        return Math.max(leftDiameter, rightDiameter) + 1;
        


    }
}
// @lc code=end

