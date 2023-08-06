#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 划重点：只能交易两次，所以涨了就买，会浪费次数
        # 画个图可以看出，挑选上升最大的两段就行，但是实际中怎么保证买入在卖出后呢

        dp = [[[0]*3 for _ in range(2)] for _ in range(len(prices))]
        # dp[i][j]的含义：在第i天j状态，剩余的钱，j=1持有股票，j=0不持有股票，这样就可以根据状态来做操作了
        # 怎么限制两次
        # dp[i][j][k]的含义：k是已操作的次数, k = 0,1,2

        for i in range(len(prices)):
            for k in range(1, 3):
                if i == 0:
                    dp[i][0][k] = 0
                    dp[i][1][k] = - prices[i]
                    continue
                dp[i][0][k] = max(
                    dp[i-1][0][k],
                    dp[i-1][1][k] + prices[i]
                )
                dp[i][1][k] = max(
                    dp[i-1][1][k],
                    dp[i-1][0][k-1] - prices[i]
                )
        return dp[len(prices)-1][0][2]
            
            

# @lc code=end

