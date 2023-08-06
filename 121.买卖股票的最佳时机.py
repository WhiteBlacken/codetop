#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')
        for i, price in enumerate(prices):
            if i != 0:
                max_profit = max(price - min_price, max_profit)
            min_price = min(min_price, price) # 后更新
        return max_profit

# @lc code=end

