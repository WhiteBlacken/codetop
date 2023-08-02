/*
 * @lc app=leetcode.cn id=26 lang=java
 *
 * [26] 删除有序数组中的重复项
 */

// @lc code=start
class Solution {
    public int removeDuplicates(int[] nums) {
        //有序的话，重复数字都在邻近
        int cur = 0,i = 0;
        while(i<nums.length){
            while(i+1<nums.length&&nums[i]==nums[i+1]){
                i++;
            }
            nums[cur] = nums[i];
            cur++;
            i++;
        }
        return cur;
    }
}
// @lc code=end

