/*
 * @lc app=leetcode.cn id=701 lang=java
 *
 * [701] 二叉搜索树中的插入操作
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
    public TreeNode insertIntoBST(TreeNode root, int val) {
        //转换成子问题，在小的子树中插入
        if(root==null)return new TreeNode(val);
        if(val > root.val){
            root.right = insertIntoBST(root.right, val);
        }else{
            root.left = insertIntoBST(root.left, val);
        }
        return root;
    }
}
// @lc code=end

