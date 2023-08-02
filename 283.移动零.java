/*
 * @lc app=leetcode.cn id=283 lang=java
 *
 * [283] 移动零
 */

// @lc code=start
class Solution {
    public void moveZeroes(int[] nums) {
        //数组移动+原地+保证顺序=双(多)指针
        int left = 0,cur = 0;
        while(left<nums.length){
            while(left+1<nums.length&&nums[left]==0)left++;
            int tmp = nums[left];
            nums[left] = nums[cur];
            nums[cur] = tmp;
            cur++;
            left++;
        }

    }
}
// @lc code=end

