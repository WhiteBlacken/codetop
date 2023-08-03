/*
 * @lc app=leetcode.cn id=322 lang=java
 *
 * [322] 零钱兑换
 */

// @lc code=start

import java.util.Arrays;

class Solution {
    public int coinChange(int[] coins, int amount) {
        //最多，最少，且不要求写出所有情况->动态规划
        int[] dp = new int[amount+1];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;
        for(int i=1;i<amount+1;i++){
            for(int coin: coins){
                if(i-coin<0||dp[i-coin]==Integer.MAX_VALUE) continue;
                dp[i] = Math.min(dp[i-coin]+1, dp[i]); //Integer.MAX_VALUE+1可以会超范围
            }
        }
        return dp[amount] == Integer.MAX_VALUE ? -1:dp[amount] ;

    }
}
// @lc code=end

