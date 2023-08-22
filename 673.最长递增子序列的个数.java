/*
 * @lc app=leetcode.cn id=673 lang=java
 *
 * [673] 最长递增子序列的个数
 */

// @lc code=start
import java.util.Arrays;
class Solution {
    public int findNumberOfLIS(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n];
        int[] path = new int[n];
        Arrays.fill(dp, 1);
        Arrays.fill(path, 1);
        int max_len = Integer.MIN_VALUE;
        for(int i=1;i<n;i++){
            for(int j=0;j<i;j++){
                if(nums[j]<nums[i]){
                    if(dp[i]<dp[j]+1){ //需要更新最大值
                        dp[i] = dp[j] + 1;
                        path[i] = path[j]; //刷新
                        max_len = Math.max(max_len, dp[i]);
                    }else if(dp[i]==dp[j]+1){//需要更新方案数
                        path[i] += path[j];
                    }
                }
            }
        }
        max_len = Math.max(max_len, 1);
        int res = 0;
        for(int i=0;i<n;i++){
            if(dp[i]==max_len)res+=path[i];
        }
        return res;
    }
}
// @lc code=end

