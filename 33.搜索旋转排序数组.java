/*
 * @lc app=leetcode.cn id=33 lang=java
 *
 * [33] 搜索旋转排序数组
 */

// @lc code=start

import java.util.Arrays;

class Solution {
    public int search(int[] nums, int target) {
        //log(n) 二分
        int idx = getMinNumIdx(nums);
        if(target>nums[nums.length-1]){
            return getTarget(Arrays.copyOfRange(nums, 0, idx), target);
        }
        int res = getTarget(Arrays.copyOfRange(nums, idx, nums.length), target);
        if(res==-1)return -1;
        return res + idx;
    }
    public int getMinNumIdx(int[] nums){
        int left = 0, right = nums.length - 1;
        int n = nums.length - 1;
        while(left<right){
            int mid = left + (right-left)/2;
            if(nums[mid]<nums[n]){
                right = mid;
            }else{
                left = mid + 1;
            }
        }
        return left;
    }
    public int getTarget(int[] nums, int target){
        int left = 0, right = nums.length - 1;
        while(left<=right){
            int mid = left + (right-left)/2;
            if(nums[mid]==target)return mid;
            if(nums[mid]>target){
                right = mid - 1;
            }else{
                left = mid + 1;
            }
        }
        return -1;
    }
}
// @lc code=end

