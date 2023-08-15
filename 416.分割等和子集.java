/*
 * @lc app=leetcode.cn id=416 lang=java
 *
 * [416] 分割等和子集
 */

// @lc code=start
class Solution {
    public boolean canPartition(int[] nums) {
        //选择：放与不放 状态：背包剩余容量，max：sum(nums)/2
        int sum_weight = 0;
        for(int num: nums)sum_weight += num;
        if(sum_weight%2!=0)return false;
        int m = nums.length, n = sum_weight/2;
        int[][] dp = new int[m+1][n+1];
        for(int i=1;i<m+1;i++){
            for(int j=1;j<n+1;j++){
                if(j-nums[i-1]<0)dp[i][j]=dp[i-1][j];
                else{
                    dp[i][j] = Math.max(
                        dp[i-1][j], 
                        dp[i-1][j-nums[i-1]]+nums[i-1]
                    );
                }
            }
        }
        return dp[m][n] == n;

    }
}
// @lc code=end

