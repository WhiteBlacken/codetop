/*
 * @lc app=leetcode.cn id=450 lang=java
 *
 * [450] 删除二叉搜索树中的节点
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
    public TreeNode deleteNode(TreeNode root, int key) {
        if(root==null)return null;
        //找到节点后，选取左子树最大值，或右子树最小值替换
        if(key>root.val){
            root.right = deleteNode(root.right, key);
        }else if(key<root.val){
            root.left = deleteNode(root.left, key);
        }else{//找到了
            if(root.left==null)return root.right;
            if(root.right==null)return root.left;
            TreeNode minNode = findMinNode(root.right);
            root.right = deleteNode(root.right, minNode.val);
            minNode.left = root.left;
            minNode.right = root.right;
            return minNode;
        }
        return root;
    }
    TreeNode findMinNode(TreeNode root){
        while(root!=null&&root.left!=null)root=root.left;
        return root;
    }
}
// @lc code=end

