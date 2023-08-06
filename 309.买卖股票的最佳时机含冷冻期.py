#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 买卖股票的最佳时机含冷冻期
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        冷冻期：只在状态转移的时候考虑即可
        划重点：可以尽可能多的交易，这个实际上股票II的进阶，所以只是中档题
        """
        n = len(prices)
        # dp[i][j] # 第i天时，持有或不持有剩余的钱 j=1-持有 j=0 未持有
        dp = [[0]*2 for _ in range(n)]
        

        for i in range(n):
            if i == 0:
                # base case
                dp[i][0] = 0
                dp[i][1] = -prices[0]
                continue
            if i == 1:
                dp[i][0] = max(
                    dp[i-1][0],
                    dp[i-1][1] + prices[i]
                )
                dp[i][1] = max(
                    dp[i-1][1],
                    -prices[i] # 必须1没有做交易
                )
                continue

            dp[i][0] = max( # 不买入就没问题
                dp[i-1][0],
                dp[i-1][1] + prices[i]
            )
            
            dp[i][1] = max(
                dp[i-1][1],
                # 如果前一天买入，则无法买入；如果卖出，也无法买入；如果既没卖出也没买入，那管他干嘛
                dp[i-2][0] - prices[i] 
            )
           
        return dp[n-1][0]


# @lc code=end

