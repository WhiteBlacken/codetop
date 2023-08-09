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
        if(root==null)return root;
        if(key==root.val){ //删除
            if(root.left==null)return root.right;
            if(root.right==null)return root.left;
            //如果左右结点都有，可以从右子树选最小结点
            TreeNode minNode = getMin(root.right);
            //将用于替换的结点删除
            root.right = deleteNode(root.right, minNode.val);
            minNode.left = root.left;
            minNode.right = root.right;
            //删除该结点
            return minNode;
        }else if(key>root.val){
            root.right = deleteNode(root.right, key);
        }else{
            root.left = deleteNode(root.left, key);
        }
        return root;
    }
    public TreeNode getMin(TreeNode node){
        while(node.left!=null)node=node.left;
        return node;
    }
}
// @lc code=end

