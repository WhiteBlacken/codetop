#
# @lc app=leetcode.cn id=714 lang=python3
#
# [714] 买卖股票的最佳时机含手续费
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        """
        股票II的进阶，转移方程时考虑手续费即可
        """
        n = len(prices)
        dp = [[0]*2 for _ in range(n)]
        for i in range(n):
            if i == 0: # base case
                dp[i][0] = 0
                dp[i][1] = -prices[i]
                continue
            dp[i][0] = max(
                dp[i-1][0],
                dp[i-1][1] + prices[i] - fee # diff
            )
            dp[i][1] = max(
                dp[i-1][1],
                dp[i-1][0] - prices[i]
            )
        return dp[n-1][0]
# @lc code=end

