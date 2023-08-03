/*
 * @lc app=leetcode.cn id=144 lang=java
 *
 * [144] 二叉树的前序遍历
 */

// @lc code=start

import java.util.LinkedList;
import java.util.List;

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
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> arrs = new LinkedList<>();
        preorder(root, arrs);
        return arrs;

    }
    public void preorder(TreeNode root,List<Integer> arrs){
        if(root==null)return;
        arrs.add(root.val);
        preorder(root.left, arrs);
        preorder(root.right, arrs);
    }
}
// @lc code=end

