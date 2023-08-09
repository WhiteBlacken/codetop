/*
 * @lc app=leetcode.cn id=654 lang=java
 *
 * [654] 最大二叉树
 */

// @lc code=start

import java.util.Arrays;

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
    public TreeNode constructMaximumBinaryTree(int[] nums) {
        //简单的模拟题
        if(nums.length==0)return null;
        int[] val = getMaxIndex(nums);
        TreeNode node = new TreeNode(val[0]);
        node.left = constructMaximumBinaryTree(Arrays.copyOfRange(nums, 0, val[1]));
        node.right = constructMaximumBinaryTree(Arrays.copyOfRange(nums, val[1]+1, nums.length));
        return node;


    }
    public int[] getMaxIndex(int[] nums){
        int max_value = Integer.MIN_VALUE;
        int index = -1;
        for(int i=0;i<nums.length;i++){
            if(nums[i]>max_value){
                max_value = nums[i];
                index = i;
            }
        }
        return new int[]{max_value, index};
    }
}
// @lc code=end

