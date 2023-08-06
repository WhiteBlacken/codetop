#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#

# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # 和买卖股票III一样，只是把2换成了3而已
        # dp[i][k][j]: 在第i天,执行k次操作，处于j状态,所剩下的钱
        n = len(prices)
        dp = [[[0]*2 for _ in range(k+1)] for _ in range(n)]

        for i in range(n):
            for q in range(1, k+1):
                if i == 0:
                    dp[i][q][0] = 0
                    dp[i][q][1] = -prices[0]
                    continue
                dp[i][q][0] = max(
                    dp[i-1][q][0], # 之前就不持有
                    dp[i-1][q][1] + prices[i] # 之前持有，今日卖出
                )
                dp[i][q][1] = max(
                    dp[i-1][q][1], # 之前就持有
                    dp[i-1][q-1][0] - prices[i] # 之前不持有，今日购入
                )
        return dp[n-1][k][0]
# @lc code=end

