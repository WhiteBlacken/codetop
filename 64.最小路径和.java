/*
 * @lc app=leetcode.cn id=64 lang=java
 *
 * [64] 最小路径和
 */

// @lc code=start

import java.util.Arrays;

class Solution {
    public int minPathSum(int[][] grid) {
        //选择，从左过来，还是从上来
        //dp[i][j]: 在位置i,j的最小路径和
        int m = grid.length, n = grid[0].length;
        int[][] dp = new int[m][n];
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(i==0&&j==0){
                    dp[i][j] = grid[i][j];
                    continue;
                }
                if(i==0){
                    dp[i][j] = dp[i][j-1] + grid[i][j];
                    continue;
                }
                if(j==0){
                    dp[i][j] = dp[i-1][j] + grid[i][j];
                    continue;
                }
                dp[i][j] = Math.min(dp[i-1][j], dp[i][j-1]) + grid[i][j];
            }
        }
        return dp[m-1][n-1];
    }
}
// @lc code=end

