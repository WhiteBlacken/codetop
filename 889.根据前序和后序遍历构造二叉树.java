/*
 * @lc app=leetcode.cn id=889 lang=java
 *
 * [889] 根据前序和后序遍历构造二叉树
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
    private int preIndex = 0;
    private int postIndex = 0;
    public TreeNode constructFromPrePost(int[] preorder, int[] postorder) {
        TreeNode root = new TreeNode(preorder[preIndex]);
        preIndex += 1;
        //如果左右子树均不存在，则前序和后序一样
        if(root.val!=postorder[postIndex]){ //左子树其实未必存在，可能为空，右子树也一样
            root.left = constructFromPrePost(preorder, postorder);
        }
        if(root.val!=postorder[postIndex]){
            root.right = constructFromPrePost(preorder, postorder);
        }
        postIndex += 1;
        return root;
    }
}
// @lc code=end

