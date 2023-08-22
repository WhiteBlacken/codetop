/*
 * @lc app=leetcode.cn id=300 lang=java
 *
 * [300] 最长递增子序列
 */

// @lc code=start
import java.util.Arrays;
class Solution {
    public int lengthOfLIS(int[] nums) {
        //因为是子序列，所以复杂度会高
        int res = Integer.MIN_VALUE;
        int n = nums.length;
        int[] dp = new int[n];
        Arrays.fill(dp, 1);
        for(int i=1;i<n;i++){
            for(int j=0;j<i;j++){
                if(nums[j]>=nums[i])continue;
                dp[i] = Math.max(
                    dp[i],
                    dp[j] + 1
                );
                res = Math.max(dp[i], res);
            }
        }
        if(res==Integer.MIN_VALUE)return 1;
        return res;
    }
}
// @lc code=end

